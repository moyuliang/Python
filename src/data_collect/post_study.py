# -*- coding: utf-8 -*-
import urllib2
from urllib2 import Request
import urllib

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = urllib.urlencode([
    ("StartStation","977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation","a7a04c89-900b-4798-95a3-c01c455622f4"),
    ("SearchDate","2018/05/28"),
    ("SearchTime","22:30"),
    ("SearchWay","DepartureInMandarin")
])

req.add_header('Origin',
               'http://www.thsrc.com.tw')
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
resp = urllib2.urlopen(req)
print(resp.read().decode("utf-8"))

