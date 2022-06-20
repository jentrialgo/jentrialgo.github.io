Title: Using IPVS in kube-proxy with eksctl
Date: 2022-06-20 12:00
Category: kubernetes, eksctl, kube-proxy
Tags: kubernetes, eksctl, kube-proxy

I have a kubernetes cluster launched with `eksctl`. I can get the configuration
of `kube-proxy` with:

    kubectl edit configmap kube-proxy-config -n kube-system

I see that the default configuration uses the `iptables` mode. In order to
change it, the `mode` parameter has to be changed to `ipvs` and the scheduler
parameter in the `ipvs` section, which is initially empty, has to be assigned one
of [these
policies](https://kubernetes.io/blog/2018/07/09/ipvs-based-in-cluster-load-balancing-deep-dive/#parameter-changes):

- rr: round-robin
- lc: least connection
- dh: destination hashing
- sh: source hashing
- sed: shortest expected delay
- nq: never queue

Notice that the corresponding kernel modules must be present in the working
node. You can connect with ssh to the node and check with modules are loaded
with:

    lsmod | grep ip_vs

In order to apply the configuration, kube-proxy has to be restarted with this
command:

    kubectl rollout restart ds kube-proxy -n kube-system

I get this:

    ip_vs_sh               16384  0
    ip_vs_wrr              16384  0
    ip_vs_rr               16384  0
    ip_vs                 176128  6 ip_vs_rr,ip_vs_sh,ip_vs_wrr
    nf_conntrack          163840  8 xt_conntrack,nf_nat,xt_state,xt_nat,nf_conntrack_netlink,xt_connmark,xt_MASQUERADE,ip_vs
    nf_defrag_ipv6         24576  2 nf_conntrack,ip_vs

This means that the modules for the policies lc and sed are not loaded. You can
load them running the following commands:

    sudo modprobe ip_vs_sed
    sudo modprobe ip_vs_lc

In my example, using a service with 7 replicas that takes around 200 ms of
processing, I see an extra 100 ms of latency added by the kube-proxy load
balancer when using the `iptables` mode, and only 4 ms of latency added when
using the `ipvs` mode, even when both are using the round-robin policy.
