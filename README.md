This is the repository for my personal blog about technology, _Giving back to
tech_. You can check it out at <http://jentrialgo.github.io>.

## Building the Blog

This blog is built using [Pelican](https://getpelican.com/), a static site generator
written in Python. The [first
post](https://jentrialgo.github.io/using-pelican-as-blogging-platform-for-github.html)
explains how to set up the blog and use GitHub Pages for hosting.

### Prerequisites

- Python 3.x
- Pelican
- ghp-import (for publishing to GitHub Pages)

Install required packages:

```bash
pip install -r requirements.txt
```

Clone the Flex theme:

```bash
git clone https://github.com/alexandrevicenzi/Flex
```

### Building on Linux

The blog can be built using the Makefile:

```bash
# Generate the site
make html

# Clean the output directory
make clean

# Regenerate files upon modification
make regenerate

# Serve the site locally (default port: 8000)
make serve

# Serve on all interfaces (as root)
make serve-global

# Serve and regenerate together
make devserver

# Regenerate and serve on all interfaces
make devserver-global

# Generate using production settings
make publish

# Upload the site to GitHub Pages
make github
```

Additional options:
- Set `DEBUG=1` to enable debugging (e.g., `make DEBUG=1 html`)
- Set `RELATIVE=1` to enable relative URLs (e.g., `make RELATIVE=1 html`)
- Set `PORT=8080` to specify a custom port (e.g., `make PORT=8080 serve`)

### Building on Windows

On Windows, you can use the `build.py` script to perform the same functions:

```bash
# Generate the site
python build.py html

# Clean the output directory
python build.py clean

# Regenerate files upon modification
python build.py regenerate

# Serve the site locally
python build.py serve

# Serve on all interfaces
python build.py serve-global

# Serve and regenerate together
python build.py devserver

# Regenerate and serve on all interfaces
python build.py devserver-global

# Generate using production settings
python build.py publish

# Upload the site to GitHub Pages
python build.py github
```

Additional options:
- Use `--debug` to enable debugging (e.g., `python build.py --debug html`)
- Use `--relative` to enable relative URLs (e.g., `python build.py --relative html`)
- Use `--port 8080` to specify a custom port (e.g., `python build.py --port 8080 serve`)
- Use `--server "127.0.0.1"` to specify a custom server address (e.g., `python build.py --server "127.0.0.1" serve-global`)
