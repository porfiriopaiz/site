#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Porfirio Páiz'
TAGLINE = '(■_■¬)'
SITEURL = 'https://porfiriopaiz.github.io/site'
USER_LOGO_URL = 'https://porfiriopaiz.github.io/site/images/prpd8Vi.png'
SITENAME = "porfirio's blog"
DISQUS_SITENAME = 'porfiriopaizsite'

# Default Path
PATH = 'content'

TIMEZONE = 'America/Managua'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_DOMAIN = SITEUR
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('About', 'https://fedoraproject.org/wiki/User:Porfiriopaiz'),
         ('Github', 'https://github.com/porfiriopaiz'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/porfiriopaiz'),
          ('Google+', 'https://plus.google.com/+PorfirioAndresPaizCarrasco'),
          ('License', 'https://creativecommons.org/licenses/by-sa/4.0/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'themes/pelican-svbhack'

# Static Path
STATIC_PATHS = [
    'images/', 
    'extra/'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# URL's
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

# Summary
SUMMARY_MAX_LENGTH = 50
