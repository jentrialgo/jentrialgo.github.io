Title: GPU sharing
Date: 2024-04-05 10:00
Category: Nvidia, GPU, Kubernetes
Tags: Nvidia, GPU, Kubernetes

I've found this [interesting post from 2022 by Nvidia about GPU sharing in
Kubernetes](https://developer.nvidia.com/blog/improving-gpu-utilization-in-kubernetes/).

The main GPU sharing technologies can be summarized in this table:

| Technology       | Description                                                                                                             | MicroArchitecture                  | CUDA Version         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------------------- |
| **CUDA Streams** | Allows concurrent operations within a single CUDA context using software abstraction.                                   | Pascal and later                   | Not specified        |
| **Time-Slicing** | Oversubscription strategy using the GPU's time-slicing scheduler.                                                       | Pascal and later                   | 11.1 (R455+ drivers) |
| **CUDA MPS**     | MPS (Multi-Process Service) enables concurrent processing of CUDA kernels from different processes, typically MPI jobs. | Not specified                      | 11.4+                |
| **MIG**          | MIG (Multi-Instance GPU) is a secure partitioning of GPUs into separate instances for dedicated resources.              | Ampere Architecture                | Not specified        |
| **NVIDIA vGPU**  | Provides VMs with simultaneous, direct access to a single physical GPU.                                                 | Compatible with MIG-supported GPUs | Not specified        |

The post also explains how GPUs are advertised as schedulable resources in Kubernetes with
the device plugin framework, but it is a integer-based resource, so it does not allow for
oversuscription. They describe a way of achieving this with time-slicing APIs.
