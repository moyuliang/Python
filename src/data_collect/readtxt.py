# -*- coding: utf-8 -*-
import ssl
import urllib.request


# urllib2.urlopen打开https时，报错
# 解决Python certificate verify failed的问题
ssl._create_default_https_context = ssl._create_stdlib_context

html = urllib.request.urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode("utf-8"))