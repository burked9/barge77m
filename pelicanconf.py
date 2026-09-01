AUTHOR = 'Daniel Burke'
SITENAME = '77M Vessel Archive'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = 'en'

# Feed settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Latest News', '/pages/news.html'),
    ('Publications & References', '/pages/references.html'),
    ('Vessels', '/pages/vessels.html'),
    ('Memories', '/pages/memories.html'),
    ('Contact', '/pages/contact.html'),
)

# Custom Theme
THEME = 'theme'

# Custom contact metadata
EMAIL = 'burked9@gmail.com'
ADDRESS = 'Whitegate, Co. Clare, Ireland'

LINKS = ()
SOCIAL = ()

DEFAULT_PAGINATION = False

# Static asset paths
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
