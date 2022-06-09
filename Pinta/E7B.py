"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E7B.py
@time:2022/5/26上午 8:59

"""

major_list=input().split()

dit={}
for i in major_list:
    dit[i]= dit.get(i, 0) + 1
datalist = list(dit.items())
datalist.sort(key=lambda x:x[1], reverse=True)#按照数量排序
for k in range(len(datalist)):
    m,n=datalist[k]
    print("{}:{}".format(m,n))
#major_dict=dict(major_list)
#print(major_dict)