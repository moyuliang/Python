# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(  # 创建连接
    host='127.0.0.1',
    port=3306,  # 端口
    user='root',  # 用户
    passwd='123456',  # 密码
    db='studyPy',  # 数据库
    charset='utf8'  # 编码
)
cursor = conn.cursor()  # 创建游标

sql_insert = "insert into user (username) values ('白玉汤') "
sql_update = "update user set username='小米' where userid=1"
sql_delete = "delete from user where userid<2"
# show variables like 'autocommit';查看当前数据库是否为自动提交模式（MySQL默认），ON为开启
# set autocommit= 0；关闭自动提交
try:
    cursor.execute(sql_insert)
    cursor.execute(sql_update)
    cursor.execute(sql_delete)

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

sql = "select * from user"
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
    print("userid=%s, username=%s" % row)

cursor.close()  # 关闭游标
conn.close()  # 关闭连接
