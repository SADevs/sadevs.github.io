#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os


AUTHOR = 'San Antonio Developers'
SITENAME = 'San Antonio Developers'
APP_NAME = os.getenv('APP_NAME', None)
if APP_NAME:
    SITEURL = f'https://{APP_NAME}.herokuapp.com'
else:
    SITEURL = 'https://sanantoniodevs.com'
THEME = 'themes/brutalist'
THEME_TEMPLATES_OVERRIDES = ['templates/']

PATH = 'content'
STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/humans.txt': {'path': 'humans.txt'}
}

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LOGO = 'sadev_500w.png'
MENUITEMS = [
    ('slack', 'https://join.slack.com/t/sanantoniodevs/shared_invite/zt-kv0j0u0x-0Yl9noVKQSLBIdl8jVg_kA'),
    ('github', 'https://github.com/SADevs/sadevs.github.io'),
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
