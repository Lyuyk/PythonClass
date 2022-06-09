"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp2B_2pointsDistance.py
@time:2022/5/12下午 4:48
@function:使用可变参数完成，示意：distance(x1,y1,z1,x2,y2,z2)
返回两点的横向距离（x轴）和空间距离
函数专门放在一个函数库文件（.py）中，函数测试代码要求输入两个点，并显示输出两个距离

"""
from math import sqrt

def distance(x1=0,y1=0,z1=0,x2=0,y2=0,z2=0):
    return abs(x1-x2),sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

def enterDis(*axis):
    list=[0 for i in range(6)]
    for i in range(len(axis)//2):
        list[i]=axis[i]
        list[3+i]=axis[len(axis)//2+i]
    return distance(*list)

