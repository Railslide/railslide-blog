#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Giulia"
SITENAME = "Railslide"
TAGLINE = "Code, experiments, and thoughts"
SITEURL = ""

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

# Avoid creating authors page, since this is a one woman show
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (
    ("github", "https://github.com/Railslide/"),
    ("rss", "feeds/all.atom.xml"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = "%d-%m-%Y"

# Static paths
STATIC_PATHS = ["CNAME", "images"]

# Theme
THEME = "themes/puremorning"


# Pages
PAGE_URL = PAGE_SAVE_AS = "{slug}.html"

# Sidebar menu
MENUITEMS = [
    ("About", "/about.html"),
    ("Categories", "/categories.html"),
]
