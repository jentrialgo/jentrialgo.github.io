Title: Pylance and mypy cannot find editable local imports
Date: 2023-06-01 14:00
Category: Pylance, Mypy, Python
Tags: Pylance, Mypy, Python

The other day, I wrote [a post]({filename}2023-05-26-pylance-missing-editable-import.md)
about how I fixed a problem with Pylance not finding a local import. It worked, but now
mypy was complaining about the same import.

The solution was installing the package in compat mode with:

```bash
pip install -e . --config-settings editable_mode=compat
```
