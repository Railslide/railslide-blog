#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Giulia'
SITENAME = 'Railslide'
TAGLINE = 'Code, experiments, and thoughts'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
        ('Jinja2', 'http://jinja.pocoo.org/'),
        ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github-square', 'https://github.com/Railslide/'),
          ('google-plus-square', 'https://plus.google.com/+GiuliaVergottini'),
          ('linkedin-square', 'https://www.linkedin.com/in/giuliavergottini'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static paths
STATIC_PATHS = [
    'CNAME',
    'images'
    ]

# Theme
THEME = 'themes/puremorning'
