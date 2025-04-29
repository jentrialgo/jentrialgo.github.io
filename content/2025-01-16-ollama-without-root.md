Title: Running Ollama in a Linux Environment Without Root Privileges
Date: 2025-01-16 12:00
Category: ollama, open-webui, AI, LLM
Tags: ollama, open-webui, AI, LLM

# Running Ollama in a Linux Environment Without Root Privileges

Running applications without root privileges is a common requirement for security and
compliance reasons, especially on shared systems or in environments where users don't have
administrative access. This guide will walk you through setting up **ollama** on a Linux
system under these constraints, using some tools like `uv` to manage Python dependencies
and configuring networking correctly. Maybe, this is not the easiest way and using Docker
could be simpler, but it's a good exercise to understand how to manage Python applications
without root privileges.

## Prerequisites

- A functional Python environment.
- Basic command-line navigation skills.
- Network access for downloading necessary files and configuring network settings.

## Step-by-step Guide

### 1. Install `uv`

Firstly, we need a tool to handle Python applications efficiently without root privileges.
The tool I used is **`uv`**. Here’s how you can install it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

This command downloads and executes the installation script for `uv`. After installing,
verify its presence using:

```bash
which uv
```

You might need to restart your terminal session to update the PATH variable.

### 2. Download Ollama Release

Next, download the appropriate ollama release for Linux environments from their official
GitHub releases page. These commands will help you download the latest version:

```
VERSION=$(curl -s https://api.github.com/repos/ollama/ollama/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
curl -LO "https://github.com/ollama/ollama/releases/download/${VERSION}/ollama-linux-amd64.tgz"
```

Alternatively, you can manually download the release by visiting the GitHub releases page
and copying the link for the latest version. For example:

```bash
curl -LO https://github.com/ollama/ollama/releases/download/vX.Y.Z/ollama-linux-amd64.tgz
```

Replace `vX.Y.Z` with the actual version number. You can find the latest release on the
[ollama GitHub releases page](https://github.com/ollama/ollama/releases).


Extract it to a directory within your home folder or another location you have write
permissions for:

```bash
mkdir -p ~/ollama
tar -xzf ollama-linux-amd64.tgz -C ~/ollama
cd ~/ollama
```

### 3. Run Ollama with Public IP

Ollama requires to be listening on a network interface that allows external connections. You can
start the ollama server using the following command:

```bash
OLLAMA_HOST=0.0.0.0:11434 ./ollama serve
```

### 4. Set Up Open Web UI

Using `uv`, we can set up Open Web UI, which provides a web interface for ollama:

```bash
UV_PYTHON=python3.13 uv init open-webui-proy
cd open-webui-proy/
```

Notice that we didn't call the project `open-webui` directly, but `open-webui-proy`. This
is because `uv` will create a folder with the same name as the project, and we want to
avoid conflicts with the `open-webui` folder created in the previous step.

Also, we specify the Python version to use with `UV_PYTHON=python3.13`. This is important
because a version lower than 3.11 will not work with `uv` and `open-webui`.

### 5. Add and Run Open Web UI

After initializing the Open Web UI project, add it as a dependency:

```bash
uv add open-webui
```

Now, you can start the server to access your ollama interface through a web browser:

```bash
uv run open-webui serve
```

### 6. Configure Network Settings in Open Web UI

By default, Open Web UI tries to connect to ollama running on `localhost`. To change this
setting, follow these steps:

1. Go to `Admin Settings` in Open WebUI.
2. Navigate to `Connections > Ollama > Manage` (click the wrench icon).
3. Add a new connection for Ollama API with your public IP and port number.

### 7. Updating Open Web UI

To update Open Web UI, you can use the following command from the `open-webui-proy`
directory:

```bash
uv sync --upgrade
```

## Conclusion

By following these steps, you can successfully set up ollama on a Linux system without
root privileges. This approach not only enhances security but also provides flexibility
across various environments.
