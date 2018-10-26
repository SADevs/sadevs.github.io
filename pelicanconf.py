#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Omar Quimbaya'
SITENAME = 'San Antonio Developers'
SITEURL = 'https://blog.sanantoniodevs.com'
THEME = 'themes/brutalist'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Slack', 'https://join.slack.com/t/sanantoniodevs/shared_invite/MjE2ODI0NDQ4NjkwLTE1MDA5MDgwODctMzcxMmZhNjE0Zg'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/SA_Devs'),
)

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
