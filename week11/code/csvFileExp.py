"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：csvFileExp.py
@time:2022/5/5上午 9:45
@function: csv文件的读写操作，使用csv模块
"""

import csv
import pprint
from jsonFileExp import *

fileName = '../dataset/aip01.csv'

with open(fileName,encoding='utf-8') as f:
    reader = csv.reader(f) # 使用csv模块的reader方法来读取csv文件
    print(type(reader))
    print(reader)
    alist= []
    for row in reader:
        alist.append(row)
    print(len(alist))
    print(alist[0]) # 表头
    pprint.pprint(alist[1:]) # 数据

    for i in range(1,len(alist)): #第一条到最后一条，表头略去
        alist[i]=dict(zip(alist[0],alist[i])) # 每行zip完后转成字典

    print(alist)
    dumpJsonData('../dataset/aip02.json',alist[1:])