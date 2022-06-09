"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E7A.py
@time:2022/5/26上午 8:43

"""
import math

import numpy as np

a=int(input())
b=int(input())
c=int(input())

if a+b<=c or a+c<=b or b+c<=a:
    print("数据错误")
else:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("{:.2f}".format(s))
"""
arr1=np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3]])
arr2=np.array([1,1,1,1])
print(arr1+arr2)
"""