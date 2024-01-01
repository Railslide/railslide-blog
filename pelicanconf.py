AUTHOR = 'Giulia'

SITENAME = 'Railslide'
TAGLINE = "Code, experiments, and thoughts"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Avoid creating authors page, since this is a one woman show
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# Pages url
PAGE_URL = PAGE_SAVE_AS = "{slug}.html"

# Sidebar menu
MENUITEMS = [
    ("About", "/about.html"),
    ("Categories", "/categories.html"),
]

# Social widgets
SOCIAL = (
    ("github", "https://github.com/Railslide/"),
    ("rss", "feeds/all.atom.xml"),
)

# Prevent CNAME from showing up in the site
STATIC_PATHS = ["CNAME", "images"]

THEME = 'themes/puremorning'
