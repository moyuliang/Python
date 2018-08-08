# -*- coding: utf-8 -*-
# @Version: Python3.6.5
# @Time: 7/11/2018 10:27 AM
# @Author  : Jacklyn

def print_directory_contents(sPath):
    '''
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径
    :param sPath:
    :return:
    '''
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents("D:\Study\思维导图")