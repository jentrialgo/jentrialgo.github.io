Title: Changing the Pelican theme to Flex
Date: 2021-09-30 22:20
Category: Blogging
Tags: Pelican, GitHub pages, Blog

In [a previous
post]({filename}2021-09-28-using-pelican-as-blogging-platform-github.md) I
explained how to use Pelican with GitHub pages but didn't explain how to change
the theme. I've changed it now to use
[Flex](https://github.com/alexandrevicenzi/Flex) and it was harder than
expected.

Most of the guides I've found talked about cloning
[pelican-themes](https://github.com/getpelican/pelican-themes) in a folder on
your system and changing the variable `THEME` to that folder. However, that
doesn't work when you are using GitHub actions to build your site because it
won't find that folder.

My solution was cloning the theme I wanted, Flex, to a folder inside the root
folder of the blog:

```bash
git clone https://github.com/alexandrevicenzi/Flex
```

Then I set in `pelicanconf.py` the variable `THEME` as follows:

```python
THEME = 'Flex'
```

In order to make it work with GitHub actions, I had to add in the file
`publi.sh`, before calling `pelican`, this line:

```bash
git clone https://github.com/alexandrevicenzi/Flex
```

After commiting and pushing, it worked.
