# -*- coding: utf-8 -*-
import math
from functools import reduce

# 高阶函数：将函数作为参数


def add(x, y, f):
    return f(x) + f(y)


print "add(25, 9, math.sqrt)=%s" % add(25, 9, math.sqrt)

# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
# 输出[1, 4, 9, 10, 25, 36, 49, 64, 81]


def f(x):
    return x * x


print "map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])=%s" % map(
    f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 字符串首字母大写
# 输出['Adam', 'Lisa', 'Bart']


def format_name(s):
    return s.capitalize()


print "map(format_name, ['adam', 'LISA', 'barT'])=%s" % map(
    format_name, ['adam', 'LISA', 'barT'])

# reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
# reduce()还可以接收第3个可选参数，作为计算的初始值。
# 2*(2*4*5*7*12)


def prod(x, y):
    return x * y


print "reduce(prod, [2, 4, 5, 7, 12],2)=%s" % reduce(prod, [2, 4, 5, 7, 12], 2)

# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
# 当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')


def is_not_empty(s):
    return s and len(s.strip()) > 0


print filter(is_not_empty, ['test', None, '',
                            'str', '  ', 'END', '\t\t123\r\n'])

# 利用filter()过滤出1~100中平方根是整数的数


def is_sqr(x):
    # 开根后变成浮点数，所以无法用是否为整数判断。可以平方后与元数值相等判断
    # if math.sqrt(x)**2==x:
    #     return x
    return math.sqrt(x) % 1 == 0  # 小数点后面为0时，对1取余才为0


print filter(is_sqr, range(1, 101))

#忽略大小写排序
def cmp_ignore_case(s1, s2):
    # if s1.lower()>s2.lower():
    #     return 1
    # if s1.lower()<s2.lower():
    #     return -1
    # if s1.lower()==s2.lower():
    #     return 0
    return cmp(s1.lower(),s2.lower())

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)



# 内层函数f()引用了外层函数calc_prod()的变量lst（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）
# 闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
# 接收一个list，返回一个函数，返回函数可以计算参数的乘积
def calc_prod(lst):
    def a(x, y):
        return x * y
    def f():
        return reduce(a, lst)
    return f


f = calc_prod([1, 2, 3, 4])
print f
print f()

# 当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3。由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i
# 因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
    #     def f():
    #          return i*i
    #     fs.append(f)
        def f(m=i):
            return m * m
        fs.append(f)

    return fs
f1, f2, f3 = count()
print f1(),f2(),f3()
