# -*- coding: utf-8 -*-
#递归函数实现汉诺塔游戏
def move(n, a, b, c):
    if n==1:
        print(a+"-->"+c)
    else:
        move(n-1,a,c,b)#把 (N-1) 个圆盘移动到 b
        print(a+"-->"+c)#将 a的最后一个圆盘移动到c
        move(n-1,b,a,c)#将b的(N-1)个圆盘移动到c
move(4, 'A', 'B', 'C')