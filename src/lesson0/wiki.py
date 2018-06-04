# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import urllib.request
import re

# 请求URL并把结果用utf-8编码
resp=urllib.request.urlopen("http://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

# 使用BeautifulSoup去解析
soup=bs(resp,"html.parser")

# 获取所有以/wiki/开头的a标签的href属性
list_url=soup.findAll("a",href=re.compile("^/wiki/"))

# 输出所有的词条对应的名称和URL
for url in list_url:
    # 过滤.jpg或.JPG结尾的URL
    if not re.search("\.(jpg|JPG)$",url["href"]):
        # 输出URL的文字和链接
        print(url.get_text(),"<---->","http://en.wikipedia.org"+url["href"])
