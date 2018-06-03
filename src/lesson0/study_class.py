# -*- coding: utf-8 -*-

#没有继承的类时，继承object类，否则python2会继承老式类
class Programmer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name  # 公有
        self._age = age  # 假设是私有，实际上是公有
        self.__weight = weight  # 假设是私有，实际上是被更改了名字

    @classmethod
    def get_hobby(self):
        return self.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print("My Name is %s \nI am %s years old\n" % (self.name, self._age))


class BackendProgrammer(Programmer):
    def __init__(self, name, age, weight, language):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print("My Name is %s \nMy favorite language is %s\n" % (
            self.name, self.language))

# 多态


def introduce(programmer):
    if isinstance(programmer, Programmer):
        programmer.self_introduction()


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    print(dir(programmer))
    print(programmer.__dict__)
    print(programmer._Programmer__weight)
    print(programmer.get_hobby())
    print(programmer.get_weight)
    programmer.self_introduction()

    backendProgrammer = BackendProgrammer('Tim', 30, 70, 'Python')
    print(dir(backendProgrammer))
    print(backendProgrammer.__dict__)
    print(type(backendProgrammer))
    print(isinstance(backendProgrammer, Programmer)) # 返回True，被判定为所属的父类

    introduce(programmer)
    introduce(backendProgrammer)
