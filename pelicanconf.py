#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kondal Rao Komaragiri'
SITENAME = u'Build Crash Repeat'
SITEURL = 'http://kondalrao.github.io/Build-Crash-Repeat'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = '%A %d %B %Y'

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
                }

# Extract post date from filename
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})'

# Sole author and don't use categories ... disable these features
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL settings
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tag-{slug}.html'
TAG_SAVE_AS = 'tag-{slug}.html'
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'

# Contact
EMAIL_ADDR = 'kondal04 at gmail dot com'

# Elegant Theme
THEME = './theme/pelican-elegant'

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [ ]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://www.github.com/kondalrao'),
          ('Linkedin', 'https://www.linkedin.com/in/kondal'),)

DEFAULT_PAGINATION = 5

# Tag cloud
TAG_CLOUD_STEPS = 4
