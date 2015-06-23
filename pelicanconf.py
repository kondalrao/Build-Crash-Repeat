#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kondal Rao Komaragiri'
SITENAME = u'Build Crash Repeat'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%A %d %B %Y'
DATE_FORMATS = {'en': '%b %d, %Y'}

# Extract post date from filename
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})'

# Plugins
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
PLUGIN_PATHS = ['./pelican-plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'latex', 'related_posts', 'assets', 'share_post',
           'series']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
TYPOGRIFY = True
THEME = './pelican-themes/elegant'
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'


# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'empty'


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

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://www.github.com/kondalrao'),
          ('Linkedin', 'https://www.linkedin.com/in/kondal'),
          ('Email', 'mailto:kondal04@gmail.com'))

DEFAULT_PAGINATION = 5

# Tag cloud
TAG_CLOUD_STEPS = 4


# Landing Page
PROJECTS = [
        {
            'name': 'Analytics',
            'url': 'https://github.com/kondalrao/Analytics',
            'description': 'Analytics using Flask, Fabric, D3JS.'
        },
        {
            'name': 'FSM Engine',
            'url': 'https://github.com/kondalrao/fsm_engine',
            'description': 'Distributed FSM Engine using XML.'
        },
        {
            'name': 'Chit Chat',
            'url': 'https://github.com/kondalrao/ChitChat',
            'description': 'Simple Chatting server using Elixir.'
        },
        {
            'name': 'Swift Calc',
            'url': 'https://github.com/kondalrao/SwiftCalc',
            'description': 'Simple calculator using Swift.'
        },
        ]

LANDING_PAGE_ABOUT = {'title': 'The Endless Cycle',
        'details': """
            <div itemscope itemtype="http://schema.org/Person">

            <p>My name is <span itemprop="name">Kondal Rao Komaragiri</span>.
            I am <a href="https://github.com/kondalrao/" title="My Github profile" itemprop="url"><span itemprop="nickname">kondalrao</span></a> at Github.
            You can also reach me via <a href="mailto:kondal04@gmail.com" title="My email address" itemprop="email">email</a>.</p>

            <p>I currently work at <a href="http://www.cisco.com/" title="Cisco" itemprop="url">Cisco</a>
            as a software engineer for N7K product line.</p>

            <p>My hobby is to design and build with 'let it crash' motto. Though I spend most of my time with C and Network Programming,
            I often try to learn new technologies and build something. I'm polyglot programmer and personally inclined in learning new languages
            and building frameworks/systems using them.</p>

            <p>Besides programming, I spend my time <a href="http://www.goodreads.com/kondal" title="My GoodReads profile" itemprop="url">reading</a>
            and spending time with my daughter and watching anime.</p></div>"""}
