"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：C4D.py
@time:2022/4/10上午 10:52

"""

data = input()
dt=data.split()
min_score=max_score=int(dt[1])
min_name=max_name=dt[0]
cnt=0
sum=0
while data:
    cnt+=1
    dt=data.split()
    if min_score>int(dt[1]):
        min_score=int(dt[1])
        min_name=dt[0]
    if max_score<int(dt[1]):
        max_score=int(dt[1])
        max_name=dt[0]
    sum+=int(dt[1])
    data=input()
avg=sum/cnt
print("最高分课程是{}{}, 最低分课程是{}{}, 平均分是{:.2f}".format(max_name, max_score, min_name, min_score, avg))