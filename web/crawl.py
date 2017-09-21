#coding: utf-8

import urlparse

class Crawler(object):
    count = 0

    def __init__(self, url):
        self.q = [url]
        self.seen = set()
