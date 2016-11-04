# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

BLOG_AUTHOR = "Martin Fischlechner, Jonathan West, Klaus-Peter Zauner"
BLOG_TITLE = "DropletKitchen"
SITE_URL = "https://DropletKitchen.github.io/"
# If not set, defaults to SITE_URL:
# BASE_URL = "https://DropletKitchen.github.io/"
BLOG_EMAIL = "dropletkitchen@gmail.com"
BLOG_DESCRIPTION = "Open Instrumentation and Howtos for Microfluidics"


DEFAULT_LANG = "en"
TRANSLATIONS = {DEFAULT_LANG: "",} # no translations

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        #("/posts/index.html", "Hints & Tips"),
        ("/pages/projects.html", "Projects"),
        #("/pages/methods.html", "Methods & Tutorials"),
        #("/galleries/index.html", "Galleries"),
        ("/archive/archive.html", "Archive"),
#       ("/categories/", "Tags"),
#       ("/rss.xml", "RSS feed"),
        ("/pages/about.html", "About"),
    ),
}

THEME="custom_theme"

POSTS = (
    ("posts/*.rst",  "posts", "post.tmpl"),
    ("posts/*.txt",  "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
    ("posts/*.org",  "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.rst",  "pages", "story.tmpl"),
    ("pages/*.txt",  "pages", "story.tmpl"),
    ("pages/*.html", "pages", "story.tmpl"),
    ("pages/*.org",  "pages", "story.tmpl"),
)

TIMEZONE = "UTC"
DATE_FORMAT = '%d.%m.%Y'

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing code listings to be processed and published on
# the site. The format is a dictionary of {source: relative destination}.
LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
    "orgmode": ('.org',),
}

# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = ''
# SHOW_BLOG_TITLE = True

WRITE_TAG_CLOUD = True
HIDDEN_TAGS = ['mathjax']
INDEX_PATH = "posts"

FRONT_INDEX_HEADER = {DEFAULT_LANG: ''}

ARCHIVE_PATH = "archive"
#ARCHIVE_FILENAME = "archive.html"
ARCHIVES_ARE_INDEXES = False


USE_BASE_TAG = False

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
REDIRECTIONS = []

# DEPLOY_COMMANDS = {
#     'default': [
#         "rsync -rav --delete output/ joe@my.site:/srv/www/site",
#     ]
# }


GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'
GITHUB_REMOTE_NAME = 'origin'
GITHUB_COMMIT_SOURCE = True


# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
from nikola import filters
FILTERS = {
   ".html": [filters.typogrify],
   ".js": [filters.closure_compiler],
   ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
}


# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
THUMBNAIL_SIZE = 180
MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
GALLERY_SORT_BY_DATE = False
PRESERVE_EXIF_DATA = False

# Images will be scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE
# options, but will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension).

IMAGE_FOLDERS = {
    'images': 'images',
}
IMAGE_THUMBNAIL_SIZE = 400


# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################


INDEXES_STATIC = False


# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# CODE_COLOR_SCHEME = 'autumn'


# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )


FEED_LINKS_APPEND_QUERY = False

LICENSE = """CC BY 4.0"""
CONTENT_FOOTER = 'Contents &copy; {date} {author}, provided under {license}.'

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# Choose third party comment system, leave blank to disable comments.
COMMENT_SYSTEM = ""
COMMENT_SYSTEM_ID = ""



STRIP_INDEXES = False
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

PRETTY_URLS = False
DEPLOY_DRAFTS = False

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra']


SHOW_SOURCELINK = True
COPY_SOURCES = True

INDEX_DISPLAY_POST_COUNT = 20

GENERATE_RSS = False
GENERATE_ATOM = False

# This will be added right before </head>:
# EXTRA_HEAD_DATA = ""
# Added to the bottom of <body> in the default template (base.tmpl).
# BODY_END = ""

UNSLUGIFY_TITLES = True
ADDITIONAL_METADATA = {  'author' : '' }


HYPHENATE = True

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
