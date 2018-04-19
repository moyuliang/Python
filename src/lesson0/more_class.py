# -*- coding: utf-8 -*-

#内建属性
class Programmer(object):
    def __new__(cls, *args, **kwargs):
        print 'call __new__ method'
        print args
        return super(Programmer, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        print 'call __init__ method'
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception("age must be int")

    def __eq__(self, other):
        if isinstance(other, Programmer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programmer')

    def __add__(self, other):
        if isinstance(other, Programmer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programmer')

    def __str__(self):
        return '%s is %s years old' % (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()

    def __getattribute__(self, name):
        # return getattr(self,name)#容易无限递归
        # return self.__dict__[name]#容易无限递归
        return super(Programmer, self).__getattribute__(
            name)  # 使用父类的getattrbute方法不容易出错

    def __setattr__(self, name, value):
        # setattr(self, name, value)#容易无限递归
        self.__dict__[name] = value


if __name__ == '__main__':
    programmer = Programmer('Albert', 25)
    print programmer.__dict__
    programmer1 = Programmer('Bill', 30)
    print programmer == programmer1
    print programmer + programmer1
    print programmer
    print dir(programmer)
    print programmer.name
