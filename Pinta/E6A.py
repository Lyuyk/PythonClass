"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E6A.py
@time:2022/6/1下午 4:02
@function:集合是一个无序的、没有重复元素的数据类型，在输出或转为序列类型时，其元素位置随机出现。

李白是一个社区大学的老师，一天，他让学生小明计算一下温室里植物的平均高度。
"""
plantHeightList=list(map(int,input().split()))
plantHeightList=list(set(plantHeightList))
sum=0
for i in plantHeightList:
    sum+=i
avr=sum/len(plantHeightList)
print("{:.3f}".format(avr))