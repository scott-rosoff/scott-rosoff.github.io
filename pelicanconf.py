#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Scott Rosoff'
SITENAME = 'scott-rosoff'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'English'
THEME = "attila"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

'''
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
 '''

# Social widget

SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/scott-rosoff-133246155/'),
          ('github', 'https://github.com/scott-rosoff'),
		  ('envelope','mailto:scrosoff@gmail.com')
		  )

AUTHORS_BIO = {
  "scott": {
    "cover": "/content/images/profile_pic.jpg",
	"location": "Seattle",
	"bio" : "This is my bio...to fill in"
  }
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True