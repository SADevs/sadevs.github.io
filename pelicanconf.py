#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'San Antonio Developers'
SITENAME = 'San Antonio Developers'
SITEURL = 'https://sanantoniodevs.com'
THEME = 'themes/brutalist'
THEME_TEMPLATES_OVERRIDES = ['templates/']

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LOGO = 'sadev500w.png'
MENUITEMS = [
    ('slack', 'https://join.slack.com/t/sanantoniodevs/shared_invite/MjE2ODI0NDQ4NjkwLTE1MDA5MDgwODctMzcxMmZhNjE0Zg'),
]

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['events']
PLUGIN_EVENTS = {
    'ics_fname': 'calendar.ics',
}

# Social widget
TWITTER = 'https://twitter.com/SA_Devs'
GITHUB = 'https://github.com/sadevs'
DISQUS_SITENAME = "sanantoniodevs"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
