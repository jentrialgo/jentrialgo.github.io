Title: Integrating Prometheus, InfluxDB and Grafana
Category: Kubernetes
Tags: Kubernetes, Prometheus, Telegraf, InfluxDB, Grafana

I've got a Kubernetes cluster prepared to be be integrated with Prometheus,
i.e., all relevant information is exposed with `/metrics` and scraped by a
Prometheus instance. I want to save the information long term and I've decided
that Influx DB is the best option for that. In addition, I want to create
dashboards using Grafana.

This would require moving the information from Prometheus to Influx DB. For
Influx DB v1, this would be acomplished by using directly remote writes in
Prometheus. However, Influx DB v2 doesn't allow this way of working. Instead,
Telegraf has to be inserted in the middle. Therefore, the whole pipeline would
be `Prometheus 🠮 Telegraf 🠮 Influx DB 🠮 Grafana`.

I'm using EKS to deploy the cluster, but these instructions should work with any
other Kubernetes cluster. I'll only assume that `kubectl` is already configured
to work with your cluster. We are going to deploy meny services, so you may
require new nodes in your cluster.

Helm
----

We'are going to use Helm for installing all the components, so first we install
helm with these commands:

```bash
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3

    chmod 700 get_helm.sh

    ./get_helm.sh
```

Influx DB
---------

To deploy Influx DB using Helm, we have to add the Influx DB helm repo and then
install it with these commands:

```bash
helm repo add influxdata https://helm.influxdata.com/

helm upgrade --install my-influxdb influxdata/influxdb2
```

Run this command, per the instructions, to obtain the password and save it in
your password manager:

```bash
echo $(kubectl get secret myinfluxdb-influxdb2-auth -o "jsonpath={.data['admin-password']}" --namespace default | base64 --decode)
```

Now, we are going to redirect the port for the Influx DB web console so that it
can be accessed from outside. Run this command:

```bash
kubectl port-forward service/my-influxdb-influxdb2 8087:80 &> forward-influx.txt &
```

If you are using Visual Studio Code as I am, you should now forward port 8087
there as well.

Open in a web browser <http://localhost:8087> and you should see the InfluxDB
console. You can log in with username `admin` and the password for Influx DB
obtained above.

We are going to use the Influx DB web console to create a token that will allow
us latter to write data from Telegraf and to read it from Grafana. In the
console, go to `Data | Tokens | Generate Token | Read/Write Token`. Select the
permissions to write and read in the `default` bucket, give the token a name and
save it. Next, select it to see it. Write it down, as we will need it later.

In case you need to check the logs of Influx DB, you can do it with this
command:

```bash
kubectl logs -f --namespace default $(kubectl get pods --namespace default -l app.kubernetes.io/name=influxdb2 -o jsonpath='{ .items[0].metadata.name }')
```

Telegraf
--------

Install Telegraf with this command:

```bash
helm upgrade --install my-telegraf influxdata/telegraf
```

Notice that, at least at the time of writing, the instructions given by helm for
running an interactive shell and obtaining the logs  are wrong because the
labels are wrong. These would be the correct commands:

```bash
kubectl exec -i -t --namespace default $(kubectl get pods --namespace default -l app.kubernetes.io/name=telegraf -o jsonpath='{.items[0].metadata.name}') /bin/sh

kubectl logs -f --namespace default $(kubectl get pods --namespace default -l app.kubernetes.io/name=telegraf -o jsonpath='{ .items[0].metadata.name }')
```

You should see some errors in the log because the output configuration of
Telegraf is wrong. We are going to fix it next.

We are going to change Telegraf's configuration, which can be carried out with
the command to edit its configmap:

```bash
kubectl edit configmap/my-telegraf
```

Remove all this part:

```bash
    [[outputs.influxdb]]
      database = "telegraf"
      urls = [
        "http://influxdb.monitoring.svc:8086"
      ]
```

And write this in its place:

```bash
    [[inputs.http_listener_v2]]
    service_address = ":1234"
    path = "/receive"
    data_format = "prometheusremotewrite"

    [[outputs.influxdb_v2]]
    urls = ["http://my-influxdb-influxdb2:80"]
    token = "$INFLUX_TOKEN"
    organization = "influxdata"
    bucket = "default"
```

You have to exchange the `$INFLUX_TOKEN` with the token that you obtained before
from the InfluxDB web console.

This prepares Telegraf to receive the information in port 1234 with the path
`/recive` and forward the data to Influx DB.

In addition, increase the value of `metric_buffer_limit` to something like
50000.

In order to make Telegraf use this new configuration, save it and run this
program that kills the pod and makes kubernetes create a new one with the new
configuration:

```bash
kubectl delete pods -l app.kubernetes.io/name=telegraf
```

Check Telegraf's logs to see that there is no problem:

```bash
kubectl logs -f --namespace default $(kubectl get pods --namespace default -l app.kubernetes.io/name=telegraf -o jsonpath='{ .items[0].metadata.name }')
```

In addition, we have to create a service so that Telegraf can be reached at
`http://my-telegraph:1234` because by default it only exposes port 8125. Change
the configuration of Telegraf's service with this command:

```bash
kubectl edit svc/my-telegraf
```

Add this in the `ports` section:

```bash
    - name: http-listener
      port: 1234
      protocol: TCP
      targetPort: 1234
```

Now, you should see with this command that Telegraf's service is also listening
in port 1234:

```bash
kubectl get services
```

Prometheus
----------

If you don't have Prometheus installed in your system yet, you can do it with
these commands:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm install my-prometheus prometheus-community/prometheus
```

Edit Prometheus configuration with this command:

```bash
kubectl edit cm/my-prometheus-server
```

Add this line, at the same level as the `global` section, i.e., inside the
`prometheus.yml` section, in order to make Prometheus write the data to
Telegraf:

```bash
    remote_write:
    - url: "http://my-telegraf:1234/receive"
```

Prometheus should read the new configuration automatically once you save it.
Run this command to see the Prometheus log:

```bash
kubectl logs -f --namespace default $(kubectl get pods --namespace default -l app=prometheus -l component=server -o jsonpath='{ .items[0].metadata.name }') prometheus-server
```

If everything is OK, you should be able to see in the `Explore` section of the
Influx DB web console a `prometheus_remote_write` section with metrics about the
cluster. If you want to plot the CPU utilization, for example, you can select
the Script editor and use this query:

```bash
import "experimental/aggregate"
from(bucket: "default")
|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
|> filter(fn: (r) => r["_measurement"] == "prometheus_remote_write")
|> filter(fn: (r) => r["cpu"] == "total")
|> filter(fn: (r) => r["_field"] == "container_cpu_usage_seconds_total")
|> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
|> aggregate.rate(every: 1m, unit: 1s)
|> yield(name: "mean")
```

Submit it and you should see some data.

Grafana
-------

Install Grafana with these commands:

```bash
helm repo add grafana https://grafana.github.io/helm-charts

helm install my-grafana grafana/grafana --set sidecar.datasources.enabled=true --set sidecar.dashboards.enabled=true --set sidecar.datasources.label=grafana_datasource --set sidecar.dashboards.label=grafana_dashboard
```

Follow the instructions to get Grafana's password:

```bash
kubectl get secret --namespace default my-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

In addition, forward port 3000 of Grafana so that you can access its web
console:

```bash
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=my-grafana" -o jsonpath="{.items[0].metadata.name}")
kubectl --namespace default port-forward $POD_NAME 3000 &> forward-grafana.txt &
```

Notice that I've changed the forward command so that it redirects its output.
Forward the port also in Visual Studio Code if you are using it and open
<http://localhost:3000> to access Grafana console.

Log in with username `admin` and the password obtained above.

Now, we are going to add InfluxDB as a source for Grafana. In Grafana's web
console, go to `Data sources | Add your first data source` and select
`InfluxDB`. Select `Flux` in the Query Language to use the new syntax. Enter
this information:

- URL: `http://my-influxdb-influxdb2`
- Uncheck the toggle in `Basic Auth`.
- Organization: `influxdata`
- Token: the one obtained from InfluxDB at the beginning. It's the same one used
  for allowing Telegraf writing in InfluxDB.

Click on `Save and test`.

Add a new Dashboard and a new panel. You can add the query given above to check
that the connection between all elements works:

```bash
import "experimental/aggregate"
from(bucket: "default")
|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
|> filter(fn: (r) => r["_measurement"] == "prometheus_remote_write")
|> filter(fn: (r) => r["cpu"] == "total")
|> filter(fn: (r) => r["_field"] == "container_cpu_usage_seconds_total")
|> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
|> aggregate.rate(every: 1m, unit: 1s)
|> yield(name: "mean")
```
