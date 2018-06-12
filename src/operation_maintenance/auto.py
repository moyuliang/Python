# -*- coding: utf-8 -*-
# @Version: Python3.6.5
# @Time: 6/12/2018 2:57 PM
# @Author  : Jacklyn

import os

import sys

if os.getuid() == 0:
    pass
else:
    print("当前用户不是root用户，请以root用户执行脚本")
    sys.exit(1)

version = input('请输入你想安装的python版本（2.7/3.6)')
if version == '2.7':
    url = 'https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz'
if version == '3.6':
    url = 'https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz'
else:
    print('您输入的版本号有误，请重新输入')
    sys.exit()

cmd = 'wget ' + url
res = os.system(cmd)
if res != 0:
    print('下载源码包失败，请检查当前网路')
    sys.exit()

if version == '2.7':
    package_name = 'Python-2.7.15'
else:
    package_name = 'Python-3.6.5'
cmd = 'tar xf ' + package_name + '.tgz'
res = os.system(cmd)
if res != 0:
    os.system('rm ' + package_name + '.tgz')
    print('解压源码包失败，请重新这个脚本下载源码包')
    sys.exit(1)

cmd = 'cd ' + package_name + ' && ./configure --prefix=/usr/local/python && make && make install'
res = os.system(cmd)
if res != 0:
    print('编译python源码失败，请检查是否缺少依赖库')
    sys.exit(1)
