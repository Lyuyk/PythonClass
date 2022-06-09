"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：ParaExample.py
@time:2022/4/28上午 9:29
@function: 1、实现模块中的函数的定义 2、参数的传递方式
"""

def square(x):
    return x**2

def cubic(x):
    return x**3

def squareAndCubic(x):
    return x**2,x**3

def Add(x,*y):
    sum=0
    sum=sum+x
    for data in y:
        sum - sum + data
    return sum

def Sum(x,y,**z):
    sum = 0
    sum = sum+x+y
    for k,v in z.items():
        sum=sum+v
    return sum

if __name__=="__main__":#模块程序驱动部分
    a=5
    print(square(a))
    print(cubic(a))
    print(squareAndCubic(a))