# -*- coding: utf-8 -*-
import codecs
import os
import shutil
import json

# **********文件读写start**********
# 以只读方式打开一个文件,将文件写入另一个文件
with codecs.open("..\..\\resource\\txt\\readfile.txt", 'r', 'gbk') as fr:
    try:
        fw = codecs.open("..\..\\resource\\txt\\writefile.txt", 'w', 'utf-8')
        for line in fr.readlines():
            fw.write(line)
    except IOError as e:
        fw.close()
        print*(e)

# 以读写方式打开文件
# f=open("writefile.txt",'r+')
# f=open("writefile.txt",'w+')
# 以追加和读写方式打开文件
# f=open("writefile.txt",'a')
# **********文件读写end**********


# **********操作文件和目录start**********

# 操作系统名字
# nt:windows
# prosix:Mac OS X,Linux,Unix
print(os.name)

# 查看环境变量
print(os.environ)

# 获取某个环境变量的值
print(os.getenv('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录
# 首先把目录的完整路径表示出来：
print(os.path.join('C:\Self\Study\Python\Python\src\lesson0', 'testfile'))
# 然后创建一个目录：
# print(*os.mkdir('C:\Self\Study\Python\Python\src\lesson0\\testfile')
# 删掉一个目录：
# print os.rmdir('C:\Self\Study\Python\Python\src\lesson0\\testfile')

# 拆分路径，后一部分总是最后级别的目录或文件名
print(os.path.split('C:\Self\Study\Python\Python\src\lesson0\lesson.txt'))

# 文件重命名
# os.rename('test.txt','test.py')

# 删掉文件
# os.remove('test.py')

# 复制文件
# shutil.copyfile('lesson0_1.py','test.py')

# 列出当前目录下所有py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# **********操作文件和目录end**********


# **********序列化start**********

# 把python对象变成一个json（序列化）
d = dict(name='Bob', age=20, score=88)

print(json.dumps(d))
# {"age": 20, "score": 88, "name": "Bob"}

# 把json变成python对象（反序列化）
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
# {u'age': 20, u'score': 88, u'name': u'Bob'}


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# 序列化student对象


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
# print json.dumps(s,default=lambda obj:obj.__dict__)
# 反序列化Student对象


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(json_str, object_hook=dict2student))

# **********序列化end**********
