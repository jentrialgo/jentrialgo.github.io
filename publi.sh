#! /bin/bash
## file: publi.sh

# install tools
sudo apt-get install -y git make python3 python3-pip python3-setuptools python3-wheel

# setup github config
git config user.email "joaquin@uniovi.es"
git config user.name "jentrialgo"

# install dependencies
sudo pip3 install -r requirements.txt

# pelican commands - install theme put your theme in themes directory
#pelican-themes --install themes/theme-name
pelican

# publish to github pages
ghp-import -m "Generate Pelican site" -b gh-pages output
git push -f origin gh-pages
