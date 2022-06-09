"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：randomNumbers.py
@time:2022/4/7上午 9:29

"""

import random
import time

def randomNumbers(number,start,end):
    # 使用列表生成number个介于start和end之间不重复随机数
    data = []
    n=0
    while True:
        element= random.randint(start,end)
        if element not in data:
            data.append(element)
            n+=1
        if n== number -1:
            break
    return data

def randomNumbers1(number,start,end):
    # 使用列表生成number个介于start和end之间不重复随机数
    data=[]
    while len(data) < number:
        element =random.randint(start,end)
        if element not in data:
            data.append(element)

def randomNumbers2(number,start,end):
    #使用列表生成number个介于start和end之间不重复随机数
    data = set()
    while len(data) < number:
        element=random.randint(start,end)
        data.add(element)
    return data


#数字范围
begin,end = 1,100000

num=5000

rep=10
for ran in (randomNumbers,randomNumbers1,randomNumbers2):
    start = time.time()
    for i in range(rep):
        ran(num,begin,end)
    print(ran.__name__,time.time()-start)