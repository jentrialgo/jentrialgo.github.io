Title: Visual Studio Code unable to connect
Date: 2023-04-21 12:00
Category: Visual Studio Code
Tags: Visual Studio Code, VS Code

Some times, I get this error:

```
Unable to connect to VS Code server: Error in request.
Error: connect ENOENT [...]
```

I always have to search for the solution, so I decided to write it down here.
From [this
issue](https://github.com/microsoft/vscode-remote-release/issues/6997), I found
that running this solves the problem:

```
VSCODE_IPC_HOOK_CLI=$(lsof | grep $USER | grep vscode-ipc | awk '{print $(NF-1)}' | head -n 1)
```
