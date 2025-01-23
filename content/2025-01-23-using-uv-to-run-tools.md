Title: Using uv to run Python tools without installing them
Date: 2025-01-25 12:00
Category: python, uv
Tags: python, uv

I wanted to run a Python tool without installing it, or preparing a virtual environment
and all that. This is now very easy with [uv](https://github.com/astral-sh/uv), using
[uvx](https://docs.astral.sh/uv/guides/tools/).

I wanted to run [markitdown](https://github.com/microsoft/markitdown), a tool to convert
various files to Markdown. I didn't want to install it, so I used `uvx`:

```bash
uvx markitdown "file_to_convert.docx" > output_file.md
```

It downloads the tool and installs it in a temporary, isolated environment.

A tool can be installed with `uv tool install`, like this:

```bash
uv tool install markitdown
```


It's very convenient.
