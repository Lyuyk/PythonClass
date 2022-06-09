"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：C3B.py
@time:2022/4/6上午 11:40

"""
list=eval(input())
Set=[]
for i in list:
    if i not in Set:
        Set.append(i)
print(*Set,sep=' ')
