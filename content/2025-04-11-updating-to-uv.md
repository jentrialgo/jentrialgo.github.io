title: Updating to uv from pip
date: 2025-04-11 12:00
category: uv, pip, python
tags: uv, pip, python

This is a short guide on how to upgrade a project from using `pip` with a
`requirements.txt` file to using Astral's `uv`. It assumes that `uv` is already installed
and that you have a project set up with a `requirements.txt` file.

Initialize uv:

```bash
uv init
```

Remove `hello.py`.

```bash
rm hello.py
```

Modify `project.toml` to update the information about the project.

Add the dependencies from `requirements.txt` to the `project.toml` file:

```bash
uv add -r requirements.txt
```

That's it! You can now use `uv` to manage your dependencies. You can run the project with:

```bash
uv run your_script.py
```

Alternatively, you can use uv sync to manually update the environment then activate it
before executing a command:

```bash
uv sync
source .venv/bin/activate
python your_script.py
```

To add new dependencies, you can use the `uv add` command:

```bash
uv add package_name
```

To upgrade a package, you can use the `uv upgrade` command:

```bash
uv lock --upgrade-package package_name
```
