title: Connecting to a Jetson Nano with Ubuntu 18.04 Using VS Code
date: 2025-03-28 12:00
category: nano, ubuntu, vscode
tags: nano, ubuntu, vscode

If you're trying to connect remotely to an NVIDIA Jetson Nano running Ubuntu 18.04 with Visual Studio Code (VS Code), you might run into a compatibility issue due to recent changes in VS Code's remote server requirements.

Starting from release **1.99 (March 2025)**, VS Code’s prebuilt remote server is only compatible with Linux distributions using **glibc 2.28 or later**. However, Ubuntu 18.04 ships with **glibc 2.27**, making it incompatible with these newer releases.

### Solution: Use an Older Version of VS Code (1.98.2)
To work around this limitation, you can use **VS Code 1.98.2**, which is the last version compatible with Ubuntu 18.04. Here’s how to do it:

### 1. Download VS Code 1.98.2 (Portable Version)
Since later versions may not work, download the **portable version** of VS Code 1.98.2 for your platform:

- **Windows (Portable)**: [Download here](https://update.code.visualstudio.com/1.98.2/win32-x64-archive/stable)
- **Other platforms**: Follow the instructions in the [VS Code FAQ](https://code.visualstudio.com/docs/supporting/faq#_previous-release-versions) to find the appropriate link.

### 2. Extract and Run VS Code
If you downloaded the Windows portable version:
- Extract the archive to a location of your choice.
- Run `Code.exe` from the extracted folder.

For Linux/macOS:
- Extract the archive.
- Run `code` from the extracted directory.

### 3. Install the Remote SSH Extension
1. Open VS Code.
2. Go to the **Extensions** marketplace (`Ctrl+Shift+X`).
3. Search for **Remote - SSH** and install it.

### 4. Configure SSH for Your Jetson Nano
Ensure that SSH is enabled on your Jetson Nano. If SSH is not installed, run:

```bash
sudo apt update && sudo apt install openssh-server
```

On your **local machine**, configure the SSH connection:

1. Open VS Code and press `Ctrl+Shift+P`.
2. Type **Remote-SSH: Open SSH Configuration File** and select it.
3. Add an entry for your Jetson Nano (modify as needed):

   ```
   Host jetson-nano
       HostName <JETSON_IP>
       User <YOUR_USERNAME>
   ```

4. Save the file.

### 5. Connect to the Jetson Nano
1. Press `Ctrl+Shift+P`.
2. Type **Remote-SSH: Connect to Host...** and select your Jetson Nano.
3. If prompted, enter your SSH password or configure SSH keys for passwordless access.

Once connected, VS Code will install the remote server version **1.98.2**, which is compatible with Ubuntu 18.04.

### Conclusion
By using **VS Code 1.98.2**, you can continue remote development on a Jetson Nano running Ubuntu 18.04 despite the recent glibc compatibility changes. If upgrading your OS is not an option, this method allows you to maintain a functional remote development workflow.
