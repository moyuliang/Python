# -*- coding: utf-8 -*-
# @Time    : 6/4/2018 2:09 PM
# @Author  : Jacklyn
import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

