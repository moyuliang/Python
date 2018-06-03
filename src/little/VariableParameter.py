# -*- coding: utf-8 -*-
def average(*args):#*args 可变参数，实际上是truple
    if len(args)==0:
        average = 0.0
    else:
        sum = 0.0
        for x in args:
            sum = sum + x
        average = sum/len(args)
    return average
print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))