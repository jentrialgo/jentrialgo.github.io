Title: Configuring Ubuntu Server 20.04 LTS gateway
Date: 2021-10-20 10:00
Category: Ubuntu
Tags: Ubuntu

The current version of Ubuntu Server 20.04 LTS uses netplan in order to
configure the network. If it doesn't use cloud-init to provision the network,
the network configuration will be in a YAML file in `/etc/netplan`. There you
can change the network parameters, such as the default gateway if you have a
fixed connection.

After changing them, run this command to apply them (remember
that you may disconnect from the network, so don't run it from a remote
connection!):

```bash
sudo netplan apply
```

A more detailed explanation can be found in [this very helpful post at
linuxize](https://linuxize.com/post/how-to-configure-static-ip-address-on-ubuntu-20-04/).
