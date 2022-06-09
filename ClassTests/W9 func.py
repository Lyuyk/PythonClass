"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：W9 func.py
@time:2022/4/23上午 10:07

"""
from functools import reduce

"""
def func(*p):return sum(p)

print(func(1, 2, 3, 4))
#print(func([1, 2, 3, 4]))
print(func(*(1, 2, 3, 4)))
print(func(*{1, 2, 3, 4}))

def showNnumber(numbers):
    for n in numbers:
         print(n)

showNnumber(3.4)

def demo(x, y, op):return eval(str(x)+op+str(y))
print(demo(3, 5, '*'))

def func(**p):return sum(p.values())
print(func(x=1, y=2, z=3))

def func(**p):return ''.join(sorted(p))
print(func(x=1, z=3, y=2))

def demo():
    x = 5
x = 3
demo()

print(x)

def chanageInt(number2):
    number2 = number2+1
    print("changeInt: number2= ",number2)

#调用
number1 = 2
chanageInt(number1)
print("number:",number1)

print(list(filter(lambda x:x>2, [0,1,2,3,0,0])))

def func(*p):return sum(p)

print(func(1, 2, 3, 4))

f=lambda x:5
print(f(3))

g = lambda x, y=3, z=5: x*y*z
print(g(1))

print(reduce(lambda x, y: x-y, [1, 2, 3]))

def chanageList(list):
    list.append(" end")
    print("list",list)

#调用
strs =['1','2']
chanageList(strs)
print("strs",strs)

formatter = 'good {0}'.format
print(list(map(formatter, ['morning'])))

print( 5 if 5>6 else (6 if 3>2 else 5) )

print(list(filter(lambda x: x>5, range(10))))
"""