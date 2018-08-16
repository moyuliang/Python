# -*- coding: utf-8 -*-
# @Version: Python3.6.5
# @Time: 8/15/2018 8:47 PM
# @Author  : Jacklyn

# 将二位列表调整格式后打印出来

def maxColWidth(tableData):
    colWidth = [0] * len(tableData)
    for i in range(len(tableData)):
        maxlen = 0
        for j in range(len(tableData[i]) - 1):
            if len(tableData[i][j]) < len(tableData[i][j + 1]):
                maxlen = len(tableData[i][j + 1])
        colWidth[i] = maxlen
    return max(colWidth)


def printTable(tableData, maxColWidth):
    maxRow=0
    for i in range(len(tableData)):
        if maxRow<len(tableData[i]):
            maxRow=len(tableData[i])

    for i in range(maxRow):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(maxColWidth), end='')
        print('\n')


tableData = [['apples', 'cherries', 'oranges', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(maxColWidth(tableData))
printTable(tableData, maxColWidth(tableData) + 2)
