title: CPUs are back (acording to Semianalysis)
date: 2026-02-18 12:00
category: CPU, GPU, Datacenters, Computer Architecture, Networks
tags: CPU, GPU, Datacenters, Computer Architecture, Networks

Semianalysis has published a [fantastic
analysis](https://newsletter.semianalysis.com/p/cpus-are-back-the-datacenter-cpu) of the
current state of CPUs and GPUs in datacenters, including a thorough history of CPUs and
GPUs in datacenters. This is my summary.

Global idea: from 2023 to 2025Q4, AI training made GPUs more important than CPUs in
datacenters. However, since then, Reinforcement Learning and vibe coding are making CPUs
more important again.

Also important: ARM is growing (with processors like AWS Graviton and Nvidia Grace), AMD
is growing and Intel is shrinking.

A brief history of CPUs and GPUs in datacenters
---------------

**1990s: origin of the modern datacenter.** The success of the PC made it possible to
sustitute costly workstations and IBM mainframes. Intel creates chips for servers:
Pentium Pro (1995) and Xeon (1998), with more cache than desktop chips.

**2000s: dot com era.** GHz race finished because of the end of Dennard scaling: around 2004 decreasing transistor size stopped proportionally improving the power consumption, so frequency could not increase further. Multicore era starts, with more cores, SMT (Simultaneous Multithreading) and multisocket systems instead of higher clock speeds. Also, increased integration: memory and I/O controllers on the same die as the CPU.

**Late 2000s: virtualization and cloud computing.** Virtualization gives rise to cloud computing hyperscalers (e.g., AWS). Customers traded CapEx for OpEx. But in 2018, Spectre and Meltdown vulnerabilities made cloud providers disable SMT, which reduced CPU performance by 20-30%, specially for Intel.

**2010s-2023: AI GPU and CPU consolidation era.** Data center around CPUs keep on growing, with COVID-19 boosting the demand for cloud services. Artificial Intelligence (AI) and Machine Learning (ML) workloads start to grow, and GPUs become more important for training large models.

ChatGPT is launched in late 2022, and the demand for AI training skyrockets. AI made GPU more important to carry out in parallel MatMuls (Matrix Multiplication), the basic operation in neural networks, optimizing throughput. CPUs are optimized for latency and code with branching, so they were less important. GPUs further optimized MatMul with Tensor cores. But still Internet traffic had to be served. CPUs split in two categories:

- **Head nodes:** they manage GPUs and fed them data. This requires high single-thread performance, with large caches and high bandwidth for memory and I/O. Dedicated CPUs for head nodes are created, such as Nvidia's Grace, with coherent memory access so that GPUs can use CPU memory for KV caches (part of LLMs). 1 CPU usually paired with 2 to 8 GPUs in each node.

- **Cloud-native CPUs:** optimized to serve Internet requests efficiently (with low throughput per Watt). Examples of substituing Intel Xeon with AMD EPYC or AWS Graviton, which are more efficient and cheaper. They have higheer number of cores, and less cache and I/O bandwidth compared to traditional CPUs.

**2025-2026: the RL and agentic era.** CPUs are needed again to process the GPU generated data. Example: Microsoft's Fairwater datacenters for OpenAI, with 1 CPU Watt per 6 GPUs Watt approximately. CPUs used in pretraining and fine-tuning to process and fed data to the GPUs. They are also used in multimodal models for image and video processing, although GPUs are integrating more and more specialized cores for accelerating these workloads. Also, CPUs are used for Reinforcement Learning (RL), where the CPU has to execute the actions (e.g., compilation in training for vibe coding) indicated by the model (which runs in the GPU) and compute the reward, without making the GPU wait. New bottleneck appears because GPUs improve in Performance per Watt faster than CPUs, so more and more CPU cores are needed to keep up with the GPU performance.

Also, RAG (Retrieval Augmented Generation) and agents are making CPUs more important because they handle this workload.

Demmand for CPUs and memory is rising. Intel has even seen depletion of their CPU inventory.

A brief history of multi-core CPU interconnects
---------------

Early multicore CPUs: two independent cores connected off-package via the front-side bus (FSB). AMD introduced in 2005 a dual-core processor with an integrated memory controller on the same die and a Network-on-Chip (NoC) interconnect for all core-to-core and core-to-memory communication. Intel's Tulsa in 2006 included a L3 shared cache between cores, which worked as a NoC. The term "data fabric" was introduced to refer to the interconnect between cores and memory (on-chip network + coherence protocol + routing and arbitration logic).

These early NoCs were limited and crossbar-based interconnects were used for higher performance, but they were expensive and not scalable (all-to-all connection). Practically, they were limited to 4 cores.

**Intel's history**


In 2010, Intel introduced the ring interconnect for Xeons, but ring architectures were already used in ATi Radeon GPUs and the IBM Cell processor. The ring connects cores in a circular fashion though their LLC (Last Level Cache). Problem: latency is not uniform between cores. Optimization: two rings with different direction. It allowed to scale up to around 10 cores, but more cores introduced latency and coherence issues. Later they created a virtual triple ring configuration.

In 2014, with 18-core CPUs, Intel used two rings connected by a switch. Using two rings introduces yet more latency and variability between cores. This was a NUMA (Non-Uniform Memory Access) architecture. Intel offered a *Cluster on Die* configuration to split the CPU into two NUMA nodes, but it was not widely used nor scalable. They got to 24 cores.

In 2016, they introduced the mesh interconnect, which is a 2D grid of routers and links. It is more scalable and has more uniform latency between cores, but it is more complex and consumes more power. It allowed to scale up to 28 cores.

With large meshes, the latency between cores can be high, so they introduced something similar to the *Cluster on Die* configuration, called *Sub-NUMA Clustering*, to split the CPU into multiple NUMA nodes.

They got to 40 cores in a 8x7 mesh with Ice Lake (2020). In Sapphire Rapids (2022) they introduced Advanced Matrix Extensions (AMX) for accelerating matrix operations, which increased core area and resulted in fewer cores per monolithic die, so they split the cores across multiple dies (what's called a chiplet design) to get to 60 cores. They created a packaging technology called Embedded Multi-die Interconnect Bridge (EMIB) to connect the dies, which is more efficient than using a large monolithic die. It uses a 8x12 mesh across four quadrants. Latency got even worse and there were many delays in launching these CPUs.

Emerald Rapids in 2023 used the same architecture but with two dice instead of four. They got to 66 cores.

Xeon 6 in 2024 introduced heterogeneous disaggregations: the I/O is separated from the cores and memory, so they can use different node size. They got to 144 cores. This CPUs were requested by hyperscalers to be used as cloud-native CPUs, but the hyperscalers preferred to use AMD EPYC and custom-designed ARM-based CPUs instead, which are more efficient and cheaper.

They are trying to continue with this approach in Clearwater Forest, but its having problems: it's not much faster and it's more expensive. This architecture introduces Foveros Direct, a 3D packaging technology that allows hybrid bonding of cores dies (using 18A nodes) atop dies containing the mesh, L3 cache and memory interface (using Intel 3 node). It has bandwidth issues.

They have an Intel's slide summarizing their disaggregation journey:

- Xeon 4th and 5th gen (Intel 7 node):
  - Tiles with I/O, memory and cores
  - EMIB
- Xeon 6th gen (Intel 7 + 3 nodes):
  - I/O tiles
  - Compute tiles with cores and memory
- Xeon 7th gen (Intel 7 + 3 + 18A nodes):
  - I/O tiles
  - Base tiles with mesh, L3 cache and memory interface
  - Compute tiles with cores
  - EMIB
  - Foveros Direct

**AMD's history**

AMD returned to the server market in 2017 with the EPYC line of CPUs, based on the Zen architecture. They use a chiplet design with up to 4 compute dies and were mocked by Intel, but AMD's approach provided 32 cores versus Intel's 28 cores, and better performance per watt. It used Infinity Fabric as interconnect, derived from the HyperTransport interconnect used in their previous CPUs. It is a scalable interconnect that can be used for core-to-core, core-to-memory and core-to-I/O communication. It doesn't have a unified L3 cache (only the 4 cores inside each die share an L3 cache)and has variable latency between cores. In a dual-socket configuration, there are four NUMA domains:

- Inter-socket
- Die-to-die MCM (multi-chip module, i.e., between the two dies in the same socket)
- Inter-CCX (core complex, i.e., between the two CCX in the same die)
- Intra-CCX (between cores in the same CCX)

This variable latency created problems for non-NUMA aware software.

```
___________________________________________________________________________
|                                SOCKET 0                                 |
|  __________________________                __________________________   |
| |          DIE 0           |              |          DIE 1           |  |
| |  ______      ______      |              |  ______      ______      |  |
| | | CCX  |    | CCX  |     |   Infinity   | | CCX  |    | CCX  |     |  |
| | |[C][C]|    |[C][C]|     | <----------/ | |[C][C]|    |[C][C]|     |  |
| | |[C][C]|    |[C][C]|     | /----------> | |[C][C]|    |[C][C]|     |  |
| | | {L3} |    | {L3} |     |    Fabric    | | {L3} |    | {L3} |     |  |
| | |______|    |______|     |              | |______|    |______|     |  |
| |__________________________|              |__________________________|  |
|             ^      \                              /      ^              |
|             |       \____________    ____________/       |              |
|      Infinity Fabric             \  /             Infinity Fabric       |
|             |       /------------    ------------\       |              |
|  ___________v______/_______                _______\______v___________   |
| |          DIE 2           |              |          DIE 3           |  |
| |  ______      ______      |              |  ______      ______      |  |
| | | CCX  |    | CCX  |     |   Infinity   | | CCX  |    | CCX  |     |  |
| | |[C][C]|    |[C][C]|     | <----------/ | |[C][C]|    |[C][C]|     |  |
| | |[C][C]|    |[C][C]|     | /----------> | |[C][C]|    |[C][C]|     |  |
| | | {L3} |    | {L3} |     |    Fabric    | | {L3} |    | {L3} |     |  |
| | |______|    |______|     |              | |______|    |______|     |  |
| |__________________________|              |__________________________|  |
|_________________________________________________________________________|
             ||                             ||
             || <--- External Infinity ---> || (Socket-to-Socket Link)
             ||          Fabric Link        ||
___________________________________________________________________________
|                                SOCKET 1                                 |
|                         (Identical 4-Die MCM)                           |
|_________________________________________________________________________|

Legend: [C] = CPU Core | {L3} = Shared L3 Cache
```

The 2019 Rome generation got to 64 cores (while Intel was still at 28 cores) by having eight 8-core Compute Dies (CCDs) using TSMC N7 nodes and a separate I/O die using older 12nm nodes. This centralized I/O is the main innovation. The cores in the CCDs could not connect directly between them, so they had to go through the I/O die. In 2021, the Milan generation increased CCX size to 8 cores and used a ring bus interconnect within the CCDs.

They kept this architecture in the 2022 Genoa and the 2024 Turing architectures. AMD's key advantage is that they only have do design a new CCD die for each generation, usually with more cores, while keeping the same I/O die.

Furture Intel Xeon processors using Diamond Rapids architecture will follow AMD's
approach of using a separate I/O die and multiple compute dies, with several NUMA nodes
and L3 domains. EMIB will not be needed for die-to-die interconnnect. Although they
could reach 256 cores, they are only planning to reach 144 cores in the next generation,
due to yield issues. They will probably have higher latencies. Also, no SMT. Intel's
rationale is that the area saved by not implementing SMT can be used to add more
E-cores, so it trades throughput for efficency. This works for desktops, but not for
datacenters.

So it looks like Intel's follows AMD's approach on separated I/O and compute dies, but
AMDs follows Intel's approach and now starts to use an equivalent to EIMB advanced
packaging technology in their next generation, called Venice. They also move to a mesh
network withing the CCD. They will have 256-core variants. They are also adding new
AVX instructions with different floating point formats for AI workloads.

It seems that AMD is increasing the performance gap over Intel.

**Nvidia's history**

Nvidia started in 2021 to design their own CPUs for datacenters, with the Grace CPU
line, focused on head nodes. Its main advantages is the unified memory access with the
GPUs using the 900GB/s bi-directional NVLink-C2C interconnect. This way, they can get
to 480 GB of memory per Grace CPU.

Grace CPUs are based in ARM designs with a 6x7 mesh network with up to 76 cores. They
are optimized for memory bandwidth but they have a microarchitectural bottleneck
related to branch prediction.

Their next CPU is Vera, with double C2C bandwidth (1.8TB/s for connecting CPUs to GPUs),
1.5 TB of memory at 1.2 TB/s for connecting to LPDDR5 RAM, a mesh of 7x13 with upt to 88
cores. They also use a chiplet design divided into a a I/O die, a compute die and four memory dies. It adds SMT.

**AWS's history**

AWS started in 2018 to design their own CPUs for datacenters, with the Graviton line, focused on cloud-native CPUs. They are based on ARM Neoverse cores and use a mesh interconnect. Graviton3 (2021) uses a chiplet design with four memory dies, two I/O dies and a central compute die with 64 cores, connected using Intel's EMIB technology.

Graviton4 gets to 96 cores and introduces dual-socket support. Graviton5, now in preview, gets to 192 cores.

**Microsoft's history**

Microsoft introduced it's first Cobalt 100 CPU in 2023 (128 cores) and Cobalt 200 in 2025 (132 cores). Of course, they are also based on ARM and they use a chiplet design with multiple dies connected via a mesh interconnect. It looks like they are used as general purpose CPU and not AI head nodes.

**Google's history**

Google introduced custom ARM-based CPUs for its cloud services in 2025: the Axion C4A (72 cores) with a 9x9 mesh and the Axion N4A (64 lower performance cores). They are used for general purpose workloads but plans to create a new version optimized for AI head nodes to feed its TPU clusters.

**Ampere's history**

Ampere Computing is a startup that designs ARM-based CPUs for datacenters, with a strong partnership with Oracle. It tried to compete with x86 CPUs with its Altra line, with up to 128 cores. It is now focusing on cloud-native CPUs with the AmpereOne line, with up to 256 cores. It uses a chiplet design with multiple dies connected via a mesh interconnect.

Ampere was adquired by SoftBank, with Oracle trying to separate from it because it was not able to compete effectively because of market timing. When they presented their first CPUs, most software was not ARM native and could not be used for general purpose and enterprise market. Hyperscalers could desing their own ARM-based CPUs and adapt their software, so Ampere was left with a small market share. Now, they are working on AI chips.

**ARM Phoenix**

ARM (majority owned by SoftBank) is having great success licensing its designs to other companies, but it is also designing its own CPUs for datacenters, with the Phoenix line. Meta, Cloudflare and OpenAI will be some of their first customers. Phoenix has a similar design to Cobalt 200. They will be used as AI head nodes.

**Huawei's history**

China is designing its own CPUs. In addition to Longson and Alibaba's Yitian, Huawei is the biggest player. It started designing ARM-based CPUs for datacenters in 2015. It
introduced the Kunpeng line 2017. The latest generation, Kunpeng 920B (2024), has
two compute dies with 80 cores each that support SMT. It also uses a chiplet design with a separate I/O die. In 2026, they will release Kunpeng 950 with promises of performance
improvement on databases. It has 192 cores with SMT and will be used by Oracle in China:
Huawei is subject to US sanctions.

**My conclusion**

This is an excelent article, with lots of detail, although sometimes it hard to get the big picture. Regarding general design trends, it seems that the industry is moving towards a chiplet design with separate I/O and compute dies, and a mesh interconnect. This allows to scale up the number of cores while keeping the complexity and power consumption manageable. However, it also introduces latency and coherence issues that need to be addressed with software optimizations and new interconnect technologies.

It seems that AMD is currently leading in terms of performance and efficiency, while Intel is struggling to keep up with the competition. Nvidia is focused on head nodes for AI workloads, while AWS, Microsoft and Google are designing their own CPUs for general purpose workloads in their datacenters. ARM is also gaining traction with its Phoenix line. Overall, it looks like CPUs are back in the spotlight in datacenters, with a lot of innovation and competition in this space.
