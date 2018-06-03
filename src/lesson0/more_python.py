# -*- coding: utf-8 -*-
import math
from functools import reduce

# 高阶函数：将函数作为参数


def add(x, y, f):
    return f(x) + f(y)


print("add(25, 9, math.sqrt)=%s" % add(25, 9, math.sqrt))

# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
# 输出[1, 4, 9, 10, 25, 36, 49, 64, 81]

print("map(lambda x:x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])=%s" % map(
    lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 字符串首字母大写
# 输出['Adam', 'Lisa', 'Bart']

print("map(lambda s:s.capitalize(), ['adam', 'LISA', 'barT'])=%s" % map(
    lambda s: s.capitalize(), ['adam', 'LISA', 'barT']))

# reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
# reduce()还可以接收第3个可选参数，作为计算的初始值。
# 2*(2*4*5*7*12)

print("reduce(lambda x,y:x*y, [2, 4, 5, 7, 12],2)=%s" % reduce(lambda x, y: x * y, [2, 4, 5, 7, 12], 2))

# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
# 当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')

print(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '',
                                                  'str', '  ', 'END', '\t\t123\r\n']))

# 利用filter()过滤出1~100中平方根是整数的数
# 小数点后面为0时，对1取余才为0

print(filter(lambda x: math.sqrt(x) % 1 == 0, range(1, 101)))

# 忽略大小写排序

print(sorted(['bob', 'about', 'Zoo', 'Credit'], lambda s1, s2:math.cmp(s1.lower(), s2.lower())))


# 内层函数f()引用了外层函数calc_prod()的变量lst（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）
# 闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
# 接收一个list，返回一个函数，返回函数可以计算参数的乘积
def calc_prod(lst):
    def a(x, y):
        return x * y

    def f():
        return reduce(a, lst)
    return f


# f = calc_prod([1, 2, 3, 4])
# print(f
# print(f()

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

#
# f1, f2, f3 = count()
# print(f1(), f2(), f3()

# 分数计算


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        if self.p > self.q:
            smaller = self.q
        else:
            smaller = self.p
        for i in range(1, smaller + 1):
            if ((self.p % i == 0) and (self.q % i == 0)):
                gys = i
        return '%s/%s' % (self.p / gys, self.q / gys)

    __repr__ = __str__


# r1 = Rational(1, 2)
# r2 = Rational(1, 4)
# print(r1 + r2
# print(r1 - r2
# print(r1 * r2
# print(r1 / r2

# 斐波那契数列


class Fib(object):
    # 把类变成跟函数一样的可调用对象
    def __call__(self, n):
        a, b = 0, 1
        L = []
        while n > 0:
            a, b = b, a + b
            L.append(a)
            n -= 1
        return L


# f = Fib()
# print(f(10)


