title: Running AI models locally
date: 2026-03-03 12:00
category: CPU, GPU, AI
tags: CPU, GPU, AI

A quick note about estimating which AI models can be run locally:

- [Can I Run AI locally](https://www.canirun.ai/) is a website that lists which AI models your system can run from information gathered using browser APIs.
- [LLMFit](https://github.com/AlexsJones/llmfit) is a terminal tool that does the same thing but it's a CLI and TUI implemented in Rust.
- [LLM Checker](https://github.com/Pavelevich/llm-checker) is a Node.js CLI tool that also tells you which models you can run locally, but it doesn't do it from system specs but actually tries to run the models (using Ollama) and see if they work. 
