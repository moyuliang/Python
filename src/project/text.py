# -*- coding: utf-8 -*-

# 逆转字符串——输入一个字符串，将其逆转并输出。
def reverse_string(a_str):
    return a_str[::-1]

# 拉丁猪文字游戏——这是一个英语语言游戏。
# 基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成“anana-bay”）
def ladin_pig(a_str):
    t = ('a','e','i','o','u')

    if a_str[0] not in t:
        return a_str[1:]+"-"+a_str[0]+"ay"

# 统计元音字母——输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。
def vowel_count(a_str):
    dic={'a':0,'e':0,'i':0,'o':0,'u':0}

    for a in a_str.lower():
        for key,value in dic.items():
            if a==key:
                dic[key]=dic[key]+1
    return dic

# 判断是否为回文——判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”。
def is_palindrome(a_str):
    if a_str==a_str[::-1]:
        return True
    return False

case = int(raw_input("Please enter a num:"))

if case==1:
    print reverse_string(raw_input("Please enter a string:"))
if case==2:
    print ladin_pig(raw_input("Please enter a word:"))
if case==3:
    print vowel_count(raw_input("Please enter a string:"))
if case==4:
    print is_palindrome(raw_input("Please enter a string:"))
