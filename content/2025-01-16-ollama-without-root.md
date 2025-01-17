Title: Running Ollama in a Linux Environment Without Root Privileges
Date: 2025-12-16 12:00
Category: ollama, open-webui
Tags: ollama, open-webui

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
GitHub releases page. The command typically looks like this:

```bash
curl -LO https://github.com/ollama/ollama/releases/download/vX.Y.Z/ollama-vX.Y.Z-linux-amd64.tar.gz
```

Replace `vX.Y.Z` with the actual version number. You can find the latest release on the
[ollama GitHub releases page](https://github.com/ollama/ollama/releases).

Extract it to a directory within your home folder or another location you have write
permissions for:

```bash
tar -xzf ollama-vX.Y.Z-linux-amd64.tar.gz -C ~/ollama
cd ~/ollama
```

### 3. Run Ollama with Public IP

To make the ollama instance accessible over a network, it needs to be run using a public
IP address. This step might require configuring your router for port forwarding or using a
service like ngrok:

```bash
OLLAMA_HOST=YOUR_PUBLIC_IP:PORT ./ollama serve
```

Ensure `YOUR_PUBLIC_IP` and the specified `PORT` are correctly configured to allow
incoming connections.

### 4. Set Up Open Web UI

Using `uv`, we can set up Open Web UI, which provides a web interface for ollama:

```bash
uv init open-webui
cd open-webui/
```

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

## Conclusion

By following these steps, you can successfully set up ollama on a Linux system without
root privileges. This approach not only enhances security but also provides flexibility
across various environments.
