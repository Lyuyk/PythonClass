"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E5C.py
@time:2022/6/1上午 11:33
@function: 键盘输入某班各个同学就业的行业名称，行业名称之间用空格间隔(回车结束输入) 。统计各行业就业的学生数量，按数量从高到低方式输出。
"""

majorList=list(input().split())
dic = {}
for key in majorList:
    dic[key] = dic.get(key,0) + 1
    ls = list(dic.items())
    ls.sort(key=lambda x:x[1],reverse=True)
for t in range(len(ls)):
    m,n=ls[t]
    print("{}:{}".format(m,n))
#dicSorted=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
#print(str(dicSorted).replace("{","").replace("}","").replace("'","").replace(" ","").replace(",","\n"))
