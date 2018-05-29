# -*- coding: utf-8 -*-
import urllib2
from urllib2 import Request

if __name__ == '__main__':
    req= urllib2.Request('http://www.baidu.com/')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    resp = urllib2.urlopen(req)
    print(resp.read().decode("utf-8"))
