Title: How GPGPU came to exist
Date: 2024-03-05 10:00
Category: GPGPU, CUDA, Nvidia, GPU
Tags: GPGPU, CUDA, Nvidia, GPU

I've been reading about the history of GPU computing in chapter 2 of "Massively Parallel
Processors" by David B. Kirk and Wen-mei W. Hwu. It's a fascinating story of how the GPU
came to be used for general-purpose computing.

The story begins in the 1990s, when the first consumer 3D graphics cards were being
developed. These cards were designed to accelerate the rendering of 3D graphics for video
games. They were able to do this by offloading the rendering work from the CPU to the GPU,
which was specifically designed for this task.

The first GPUs were fixed-function, meaning that they could only perform a limited set of
operations. However, as the demand for more realistic and complex graphics grew, the
capabilities of the GPU were expanded. This led to the development of programmable
shaders, which allowed developers to write custom code to control the rendering process.
In the beginning, these shaders were still limited to graphics-related tasks and there
were different kinds, such as vertex shaders and pixel shaders.

One of the questions I had when I read about CUDA cores, was this: are they independent of
the pixel and vertex shaders? Well, what happened was that GPUs evolved to have an array a
processing cores that could be used as pixel or vertex shaders. Then, the idea of using
these cores for general-purpose computing started to emerge. This was the beginning of
GPGPU. So the answer to my question is that CUDA cores are the same as pixel and vertex
shaders, but when those cores are used for general-purpose computing instead of shaders.

When the idea of using GPUs for general-purpose was proposed, one of the limitations was
that the memory addressing was very limited. The first GPUs were designed to work with
textures and frame buffers, which have a very specific memory access pattern. In
particular, pixel shaders could not access memory randomly. This was a major limitation
for general-purpose computing, which requires random access to memory. When NVIDIA
introduced random load and store instructions in the Tesla architecture, it was a major
step forward for GPGPU.
