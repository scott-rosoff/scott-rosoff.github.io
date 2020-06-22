#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Scott Rosoff'
SITENAME = 'scott-rosoff'
SITEURL = 'https://scott-rosoff.github.io'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'English'
THEME = "C:/Users/rosof/scott-rosoff.github.io/pelican-themes/pelican-bootstrap3"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATH = 'plugins/pelican-plugins'
PLUGINS = ['pelican_javascript', 'i18n_subsites']

# tell pelican where your custom.css file is in your content folder
STATIC_PATHS = ['css/my_styles.css']

# tell pelican where it should copy that file to in your output folder
EXTRA_PATH_METADATA = {
'css/my_styles.css': {'path': 'static/my_styles.css'}
}

# tell the custom theme where to find the custom.css file in your output folder
CUSTOM_CSS = 'static/my_styles.css'

CSS_OVERRIDE = ['static/my_styles.css']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Blogroll
'''
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
 '''

# Social widget

SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/scott-rosoff-133246155/'),
          ('Github', 'https://github.com/scott-rosoff'),
		  ('Email','mailto:scrosoff@gmail.com')
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