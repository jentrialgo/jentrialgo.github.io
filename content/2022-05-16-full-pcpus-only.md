Title: Pinning CPUs in Kubernetes using full-pcpus-only with eksctl
Date: 2022-05-16 12:00
Category: kubernetes, eksctl
Tags: kubernetes, eksctl

I was trying to use the option `full-pcpus-only` with eksctl and I was not
having luck. In the end, I was able to do it by using this `cluster.yaml`
configuration file:

```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: k8s-Stokholm-Cluster
  region: eu-north-1

nodeGroups:
  - name: ng-1
    instanceType: c5.4xlarge
    desiredCapacity: 1
    ssh:
      publicKeyPath: /home/joaquin/k8s/joaquin-k8s-stockholm.pub
    kubeletExtraConfig:
      cpuManagerPolicy: static
      cpuManagerPolicyOptions:
        full-pcpus-only: "true"
      kubeReserved:
        cpu: "300m"
        memory: "300Mi"
        ephemeral-storage: "1Gi"
      kubeReservedCgroup: "/kube-reserved"
      systemReserved:
        cpu: "300m"
        memory: "300Mi"
        ephemeral-storage: "1Gi"
      featureGates:
        CPUManager: true
        CPUManagerPolicyOptions: true
```

When my file had not the correct options, the problem I was seeing was that
eksctl got stuck with the message:

```text
waiting for at least 1 node(s) to become ready in "ng-1"
```

For debugging the errors, I connected by ssh to the EC2 instance that was
created and I check the logs of the kubelet service with this command:

```bash
journalctl -u kubelet.service
```

In order to have the CPUs pinned to a physical CPU, I had to make the requests
and the limits equal (both for CPU and memory). Also, the number of CPUs had to
be 2; if not, I got an `SMTAlignmentError` when launching the pod.
