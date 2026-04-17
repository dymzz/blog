#!/usr/bin/env python
# -*- coding: utf-8 -*-

SITENAME = "我的博客"
SITEURL = ""

PATH = "content"

TIMEZONE = "Asia/Shanghai"

DEFAULT_LANG = "zh"

DEFAULT_LOCALE = "zh_CN"

DEFAULT_METADATA = {
    "lang": "zh",
}

THEME = "theme"

TEMPLATE_PAGES = {
    "homepage.html": "index.html",
}

ARTICLE_URL = "posts/{slug}.html"
ARTICLE_SAVE_AS = "posts/{slug}.html"
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"

CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"

TAG_URL = "tag/{slug}.html"
TAG_SAVE_AS = "tag/{slug}.html"

TAGS_URL = "tags.html"
TAGS_SAVE_AS = "tags.html"

ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = "archives.html"

AUTHOR_URL = "author/{slug}.html"
AUTHOR_SAVE_AS = "author/{slug}.html"

INDEX_SAVE_AS = "blog/index.html"

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives"]

PAGINATED_TEMPLATES = {"index": 10}

DEFAULT_PAGINATION = 10

PAGINATION_PATTERNS = (
    (1, "blog/", "blog/index.html"),
    (2, "blog/{number}/", "blog/{number}/index.html"),
)

MONTH_ARCHIVE_URL = "archives/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/index.html"

YEAR_ARCHIVE_URL = "archives/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "archives/{date:%Y}/index.html"

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TAG_FEED_ATOM = "feeds/{slug}.atom.xml"

SITEDESCRIPTION = "一个关于技术与生活的个人博客"

SITE_SUBTITLE = "记录技术与生活"

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = [
    ("首页", "/"),
    ("博客", "/blog/"),
    ("标签", "/tags.html"),
    ("归档", "/archives.html"),
    ("项目", "/pages/projects.html"),
    ("关于", "/pages/about.html"),
]

STATIC_PATHS = ["images"]

USE_FOLDER_AS_CATEGORY = True

DEFAULT_CATEGORY = "未分类"

DELETE_OUTPUT_DIRECTORY = True

RELATIVE_URLS = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {
            "title": "目录",
            "permalink": True,
        },
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
        },
        "markdown.extensions.extra": {},
    },
    "output_format": "html5",
}
