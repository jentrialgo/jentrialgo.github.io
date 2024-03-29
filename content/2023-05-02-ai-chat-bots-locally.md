Title: Projects to test AI chat bots locally
Date: 2023-05-02 14:00
Category: AI, chat bots, Python, LLM
Tags: AI, chat bots, Python, LLM, ChatAI, ColossalChat, LocalAI, Text generation web UI, MLC LLM

Many people is interested in trying AI (Artificial Intelligence) chat bots
locally, but they don't know how to start. These are some projects that I've
found that can be used to test different LLMs (Language Learning Models) and
chat bots:

- [Text generation web UI](https://github.com/oobabooga/text-generation-webui).
  It tries to be the
  [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
  of text generation. Based on Gradio, it provides a web interface to test
  different LLMs.

- [Serge](https://github.com/nsarrazin/serge). It's an interface based on
  Svelte as web framework and llama.cpp for running mmodels. It's dockerized.
  It also provides an API.

- [openplayground](https://github.com/nat/openplayground). Works with local
  models and remote APIs. Can be installed as a Python package or run with
  Docker. It's implemented as a Flask application with a React frontend.

- [ChatAI](https://github.com/Capsize-Games/chatai). It is a desktop application
  for Windows and Ubuntu developed in Python with PyQt. It uses a Google T5-Flan
  model and it is based on [A. I.
  Runner](https://github.com/Capsize-Games/airunner), a framework to run AI
  models.

- [ColossalChat](https://github.com/hpcaitech/ColossalAI). ColossalAI provides a
  set of tools to develop deep learning models, and it includes ColossalChat,
  which is a chat bot based on LLaMA models, working for English and Chinese.
  They say in [this
  article](https://medium.com/pytorch/colossalchat-an-open-source-solution-for-cloning-chatgpt-with-a-complete-rlhf-pipeline-5edf08fb538b)
  it's the first open source solution with a whole RLHF (Reinforcement Learning
  with Human Feedback) pipeline to improve the chat bot, in the same way as
  ChatGPT. It looks like the focus is on providing tools to speed up training
  and inference.

- [LocalAI](https://github.com/go-skynet/LocalAI). Based on
  [llama.cpp](https://github.com/ggerganov/llama.cpp),
  [gpt4all](https://github.com/nomic-ai/gpt4all) and
  [ggml](https://github.com/ggerganov/ggml), it provides a local API to LLMs.
  Basically, it uses docker to deploy a web server developed in Go.

- [MLC LLM](https://github.com/mlc-ai/mlc-llm). It's a project to deploy LLMs on
  everyone's devices. It compiles the LLMs using [Apache TVM
  Unity](https://github.com/apache/tvm/tree/unity). They even have a project to
  deploy LLMs on web browsers, [Web
  LLM](https://github.com/mlc-ai/web-llm/tree/main).
