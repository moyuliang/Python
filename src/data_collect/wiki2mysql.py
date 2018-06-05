# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import ssl
import pymysql.cursors

# urllib2.urlopen打开https时，报错
# 解决Python certificate verify failed的问题
ssl._create_default_https_context = ssl._create_stdlib_context

# 请求URL并把结果用utf-8编码
resp = urllib.request.urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

# 使用BeautifulSoup去解析
soup = bs(resp, "html.parser")

# 获取所有以/wiki/开头的a标签的href属性
list_url = soup.findAll("a", href=re.compile("^/wiki/"))

# 输出所有的词条对应的名称和URL
for url in list_url:
    # 过滤.jpg或.JPG结尾的URL
    if not re.search("\.(jpg|JPG)$", url["href"]):
        # 输出URL的文字和链接
        print(url.get_text(), "<---->", "http://en.wikipedia.org" + url["href"])

        # 获取数据库链接
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     db='studypy',
                                     charset='utf8mb4')

        try:
            # 获取回话指针
            with connection.cursor() as cursor:
                # 创建sql语句
                sql = "insert into `urls`(`urlname`,'urlhref`) values(%s,%s)"

                # 执行sql语句
                cursor.execute(sql, url.get_text(), "http://en.wikipedia.org" + url["href"])

                # 提交
                connection.commit()
        finally:
            connection.close()
