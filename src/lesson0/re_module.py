# -*- coding: utf-8 -*-
import re
#python正则表达式

str1='imooc python'

#r代表原字符串，不转义特殊字符
#re.IGNORECASE忽略大小写
pa=re.compile(r'imooc',re.IGNORECASE)

ma = pa.match(str1)

print(re.match(r'[_a-zA-Z]+[_\w]*','_htll').group())

print(re.match(r'^[a-zA-Z0-9]{6,10}@(163|126|qq).com$','imoocedu@qq.com').group())

# ^匹配字符串开头
# $匹配字符串结尾

print(re.match(r'\Aimooc[\w]*','imoocpython').group())

# 匹配0-100
print(re.match(r'[1-9]?\d$|100','9').group())

# 匹配<book>python</book>
# (ab) 括号中表达式作为一个分组
# \<number>  引用编号为num的分组匹配到的字符串
print(re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>').group())

# (?P<mark>) 给分组取别名
# (?P=mark)引用分组
print(re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>python</book>').group())

re.split(r':| ','imooc:C C++ Java Python')