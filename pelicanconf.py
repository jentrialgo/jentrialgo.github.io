#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "J.E."
SITENAME = "Giving back to tech"
SITEURL = "https://jentrialgo.github.io"

PATH = "content"

TIMEZONE = "Europe/Madrid"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Personal page", "https://jentrialgo.github.io/personal-website/"),
    ("GitHub page", "https://github.com/jentrialgo"),
    ("All posts", "/archives.html"),
)

# Social widget
SOCIAL = (
    (
        "Linked.in",
        "https://www.linkedin.com/in/joaqu%C3%ADn-entrialgo-casta%C3%B1o-8a74714b/",
    ),
)

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "Flex"

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"

MAIN_MENU = True
MENUITEMS = [
    ("About", "./pages/about.html#about"),
    ("Tags", "/tags.html"),
]

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 175

SITELOGO = "images/profile.jpg"
SITETITLE = "Giving back to tech"

REL_CANONICAL = True

ARCHIVES_SAVE_AS = "archives.html"
