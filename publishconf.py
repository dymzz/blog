#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

SITEURL = os.environ.get("SITEURL", "")

RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
