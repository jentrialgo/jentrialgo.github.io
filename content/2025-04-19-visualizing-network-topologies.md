title: Visualizing Network Topologies
date: 2025-04-19 12:00
category: network, topology, visualization, javascript, vibe coding
tags: network, topology, visualization, javascript, vibe coding

While preparing my classes on interconnection networks in computer systems, I wanted to better understand metrics related to ring topologies. To explore this, I created a simple JavaScript program to visualize a ring network, using “[vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)”—an approach where you let Artificial Intelligence (AI) generate the code for you. The result is this [Ring Network Visualization](https://jentrialgo.github.io/ring-network-visualization/) ([GitHub repository](https://github.com/jentrialgo/ring-network-visualization)).

Later, I came across several impressive visualizations built with Three.js (like [this](https://x.com/nasimuddin01/status/1899411762811965533) and [this](https://x.com/renderfiction/status/1905998185962643767)), and I wanted to give it a try. Using the same “vibe coding” approach, I developed this [Topology Visualizer](https://jentrialgo.github.io/topo_visualizer/) ([GitHub repository](https://github.com/jentrialgo/topo_visualizer)). It’s a simple tool that allows you to visualize different network topologies—such as ring, mesh, and hypercube—in 3D. You can change the number of nodes and observe how the topology evolves. Clicking on a node triggers a visual effect that shows light bolts connecting it to the farthest node, effectively highlighting the diameter of the topology.

![Topology Visualizer Screenshot](https://raw.githubusercontent.com/jentrialgo/topo_visualizer/main/screenshot.png)
