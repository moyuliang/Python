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


# 一个猜数字的游戏，随机生成一个数字，给玩家10次猜测机会


def random_game():
    guesses_times = 1;

    secret_number = random.randint(0, 100)

    print("I am thinking of a number between 1 and 100.")

    while guesses_times < 10:
        try:
            guess = int(input("Take a guess:"))
        except ValueError as e:
            print("Input Error\n")
            continue

        if guess > secret_number:
            guesses_times += 1;
            print("Your number is bigger than right number:", guess)
        elif guess < secret_number:
            guesses_times += 1;
            print("Your number is smaller than right number:", guess)
        else:
            break

    if guess == secret_number:
        print('Good job! You guessed my number in ' + str(guesses_times) + ' guessed!')
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number))
    print("\n")


# 读取一段文章，将英文单词取出到一个列表中

def read_word(text):
    if (isinstance(text, str)):
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


# 参数是偶数则返回number//2，奇数则返回3*number+1

def collatz(number):
    try:
        if (number % 2 == 0):
            print(number // 2)
            return number // 2
        elif (number % 2 == 1):
            print(3 * number + 1)
            return 3 * number + 1
    except ValueError:
        print("Input Error")


# 对collatz函数不断调用，直到返回值为1

def use_collatz():
    while True:
        try:
            number = int(input("Enter number:"))
            # 整数不为零则开始递归调用
            if (number != 0):
                number = collatz(number)
                while (number != 1):
                    number = collatz(number)
            # 输入0则退出循环，结束调用
            elif (number == 0):
                break
        except ValueError:
            # 输入非整数则提示输入错误
            print("Input Eroor! ")
            continue


# 一个随机小游戏
def magic8Ball2():
    messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later',
                'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very dobtful']

    print(messages[random.randint(0, len(messages) - 1)])


# 逗号代码
def list2str(spam):
    spam[-1] = 'and ' + spam[-1]
    return ', '.join(spam)

# 字符图网格
def listandlist():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['0', '0', '0', '0', '0', '.'],
            ['.', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for j in range(0, 5):
        for i in range(0, 8):
            print(grid[i][j], end='')
        print(grid[i][j])



while True:
    case = int(
        input(
            "1.逆转字符串\t2.拉丁猪文字游戏\t3.统计元音字母\t\t4.判断回文\t5.猜数字\t"
            "6.统计文章中单词次数\t7.Collatz序列\t8.magic8Ball2\t9.逗号代码\t10.字符图网格"
            "0.退出\n"
            "Please enter a num:"))

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
    if case == 7:
        use_collatz()
    if case == 8:
        magic8Ball2()
    if case == 9:
        print(list2str(['apples', 'bananas', 'tofu', 'cats']))
    if case==10:
        listandlist()
    if case == 0:
        print("已退出游戏")
        break
