# -*- coding: utf-8 -*-
import pymysql.cursors

# 获取连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             db='pystudy',
                             charset='utf8mb4')

try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 查询语句
        sql = "select `urlname`,`urlhref` from `urls` where `id` is not null"
        count = cursor.execute(sql)
        print(count)

        # 查询数据
        result = cursor.fetchmany(size=3)
        print(result)

finally:
    connection.close()
