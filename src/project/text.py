# -*- coding: utf-8 -*-

# 逆转字符串——输入一个字符串，将其逆转并输出。
import random
import codecs
import re



def reverse_string(a_str):
    return a_str[::-1]

# 拉丁猪文字游戏——这是一个英语语言游戏。
# 基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成“anana-bay”）


def ladin_pig(a_str):
    for i, value in enumerate(a_str):
        if value not in ('a', 'e', 'i', 'o', 'u'):
            return a_str[:i] + a_str[i + 1:] + "-" + a_str[i] + "ay"
    return False

# 统计元音字母——输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。


def vowel_count(a_str):
    dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for a in a_str.lower():
        for key, value in dic.items():
            if a == key:
                dic[key] = dic[key] + 1
    return dic

# 判断是否为回文——判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”。


def is_palindrome(a_str):
    if a_str == a_str[::-1]:
        return True
    return False

# 一个猜数字的游戏，随机生成一个数字，提示用户输入的数字与生成数字比较大小的结果，知道用户猜中生成数字为止


def random_game():
    num = random.randint(0, 100)

    while True:
        try:
            guess = int(input("Please enter a number in 1~100:"))
        except ValueError as e:
            print("Input Error\n")
            continue

        if guess > num:
            print("Your number is bigger than right number:", guess)
        elif guess < num:
            print("Your number is smaller than right number:", guess)
        else:
            print("Guess right,Game Over!")
            break
        print("\n")


# 读取一段文章，将英文单词取出到一个列表中

def read_word(text):
    if(isinstance(text, str)):
        filter_str = filter(lambda x: x and x.isalpha(), re.split('[,|\.|?|!| |"|\n]+', text))
        mylist = [item for item in filter_str]
    return mylist

# 通过文件完整路径读取文件，将其中的单词和出现次数放入一个字典中

def read_file(filepath):
    mylist = []
    with codecs.open(filepath, 'r', 'utf-8') as fr:
        for line in fr.readlines():
            mylist = mylist + read_word(line)
    mydict = {}
    for i in mylist:
        if mylist.count(i) >= 1:
            mydict[i] = mylist.count(i)
    return mydict

# 统计文件中的单词和出现次数并写入特定文件中


def write_dic(filepath):
    mydict = read_file(filepath)
    with codecs.open("..\..\\resource\\txt\\write_dic.txt", 'w', 'utf-8') as fw:
        fw.write("文章中出现的单词及次数为:\n")
        for i in mydict:
            fw.write(i + " : " + str(mydict[i]) + "\n")
    print('统计完成，请查看write_dic.txt文件！')


while True:
    case = int(input("1.逆转字符串\t2.拉丁猪文字游戏\t3.统计元音字母\t\t4.判断回文\t5.猜数字\t6.统计文章中单词次数\t0.退出\nPlease enter a num:"))

    if case == 1:
        print(reverse_string(input("Please enter a string:")))
    if case == 2:
        print(ladin_pig(input("Please enter a word:")))
    if case == 3:
        print(vowel_count(input("Please enter a string:")))
    if case == 4:
        print(is_palindrome(input("Please enter a string:")))
    if case == 5:
        random_game()
    if case == 6:
        write_dic(input("Please enter a file path:"))
    if case == 0:
        print("已退出游戏")
        break
