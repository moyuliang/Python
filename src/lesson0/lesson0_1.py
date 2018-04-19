# -*- coding: utf-8 -*-
# 给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
import json
import types


def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'


class Person(object):
    count = 0

    def __init__(self, name, gender,**kw):
        self.name = name
        self.gender = gender
        Person.count = Person.count + 1
        for k,v in kw.items():
            setattr(self,k,v)


# del p1.address 删除实例属性
# 不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。而是给实例绑定了一个实例属性
p1 = Person('Alice','Female',score=90)
print "第%s个被创建的实例" % Person.count
# 方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 types.MethodType() 把一个函数变为一个方法
# 给一个实例动态添加方法并不常见，直接在class中定义要更直观。
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)

print p1.get_grade()
print p1.score

p = Person('Bob', 'Male', age=18, course='Python',score=80)
print "第%s个被创建的实例" % Person.count
# 没有绑定方法，所以调用会出错
# print p2.get_grade()
# AttributeError: 'Person' object has no attribute 'get_grade'

p3 = Person('Tim', 'Male',score=48)
print "第%s个被创建的实例" % Person.count

class Students(object):
    def __init__(self):
        pass
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()

print json.load(s)
#[u'Tim', u'Bob', u'Alice']