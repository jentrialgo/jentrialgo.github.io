Title: Using Pelican as blogging platform for GitHub
Date: 2021-09-28 22:20
Category: Blogging

So I guess my first blog should be about setting up this blog.

I wanted to use GitHub pages. By default they use Jekyll, which is built with
Ruby. I have no experience with that language, so I tried to use something
Python-based. I found [this post about using
Pelican](https://avinal.space/posts/development/twilight-blog.html), but I had
some problems. I'm going to try to give here step by step instructions, using
Linux.

Create a directory for the blog, an environment and activate it:

```bash
mkdir blog
cd blog
python -m venv .venv
source .venv/bin/activate
````

Install pelican with one of these options:

```bash
# This option only allows reStructuredText
python -m pip install pelican

# This allows markdown and reStructuredText
python -m pip install "pelican[markdown]"
```

Create the basic structure:

```bash
pelican-quickstart
```

I'll leave the standard theme. Read in the [mentioned
post](https://avinal.space/posts/development/twilight-blog.html) if you want to
change the theme.

To test locally the blog, generate the site with:

```bash
make html
```

Now start a web server with:

```bash
make serve
```

You can see the default blog in <http://localhost:8000>.

In order to add content, you should create your files in the `content`
directory. For instance, you can create an `about.md` file with this content:

```md
Title: About
Date: 2021-09-28 20:20
Category: About

About
-----

This is just a blog.
```

You can make the html again and serve it to test it locally, but the idea is
using GitHub actions so that when this code is push to a repository, the
website is generated.

Create a file called `publi.sh` with this content (change the email and the user
name):

```bash
#! /bin/bash

# install tools
sudo apt-get install -y git make python3 python3-pip python3-setuptools python3-wheel

# setup github config
git config user.email "YOUR_E_MAIL"  # Change this
git config user.name "YOUR_USERNAME" # Change this

# install dependencies
sudo pip3 install -r requirements.txt

# pelican commands - install theme put your theme in themes directory
#pelican-themes --install themes/theme-name
pelican

# publish to github pages
ghp-import -m "Generate Pelican site" -b gh-pages output
git push -f origin gh-pages
```

Notice that here I had to make changes from the instructions in the original
post. Another piece of information I found missing in the original post is that
you have to create the `requirements.txt` file with this command:

```bash
pip freeze > requirements.txt
```

Add and `.ignore` file with this content:

```gitignore
*~
._*
*.lock
*.DS_Store
*.swp
*.out
*.py[cod]
output
```

Now, create a repository in GitHub with the name `USERNAME.github.io`, using
your user name instead of `USERNAME`. Follow the instructions in GitHub to
import the files in your directory as the content of the repository. Basically,
it should be something like this:

```bash
# Create repository
git init -b main

# Add and commit current files
git add .
git commit -m "Initial structure"

# Add the GitHub repo as a remote
git pull --set-upstream origin main

# Push the files to the remote
git push -u origin main
```

Go to the GitHub page of the repository and then to the `Actions` section and
click on `Set up a workflow yourself`. Then, paste this code and commit it:

name: Publish Blog
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: set up permissions
        run: chmod +x publi.sh
      - name: Run a multi-line script
        run: ./publi.sh

Now, pull the changes to your local repo:

```bash
git pull
```

In the GitHub interface, you should be able to see in the branch `gh-pages` the
content of your blog, i.e., the HTML, CSS and javascript files that you also
obtain in your local `output` directoy when you run `make html`.

Go to the settings in your GitHub repo, select the `Pages` option in the menu
and in the `Source` section, indicate that your source is the branch `gh-pages`.
Check that it is using the `root` directory of this branch.

If everything is correct, you should be able to see your blog by going to
`USERNAME.github.io`.

If you want to add new content, create a new file in the `content` folder, be
sure to use the basic fields required for pelican (you can see then in the
example `about` post above), add and commit the file and (after testing
locally if you want), push the files to the remote directory. After the GitHub
action has finished you should be able to see your new post in your GitHub page.