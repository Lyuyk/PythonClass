"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：C3A.py
@time:2022/4/6上午 11:23

"""
data=input()
age = 0
count = 0
male = 0
while data:
    data_list=data.split()
    age += int(data_list[2])
    count += 1
    if data_list[1] == '男':
        male += 1
    data = input()
avgAge= age / count
print("平均年龄是{:.2f} 男性人数是{}".format(avgAge,male))

