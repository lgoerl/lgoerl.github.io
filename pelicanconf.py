#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lee Goerl'
SITENAME = u'Data and science'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Bryan Bischof', 'http://bbischof.com/'),
         ('Eric Bunch', 'ericbunch.org'),
         ('Will Chernoff', 'https://willchernoff.com'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/lgoerl'),
          ('instagram', 'https://www.instagram.com/hruimfinethx/'),
          ('linkedin', 'linkedin.com/in/lgoerl'),
          ('github', 'https://github.com/lgoerl'))

DEFAULT_PAGINATION = 10
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
