Title: Pylance cannot find editable local import
Date: 2023-05-27 8:00
Category: Pylance, Python
Tags: Pylance, Python

I had a problem with Pylance not finding a local import. I had installed the package in
editable mode with `pip install -e .` and it was working fine in the terminal, but Pylance
was not able to find it.

The solution was installing the package in strict mode with:

```bash
pip install -e . --config-settings editable_mode=strict
```

I got there from [this troubleshooting
page](https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#editable-install-modules-not-found)
and [this
explanation](https://setuptools.pypa.io/en/latest/userguide/development_mode.html#strict-editable-installs)
in the Setuptools documentation.
