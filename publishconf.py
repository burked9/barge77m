import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Production URL (GitHub Pages default or custom domain)
SITEURL = 'https://burked9.github.io/barge77m'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
