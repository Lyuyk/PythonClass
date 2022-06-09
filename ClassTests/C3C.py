"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：C3C.py
@time:2022/4/6上午 11:49

"""



scoreList=map(int,input().split())
A=0
B=0
C=0
D=0
F=0
for score in scoreList:
    if 90 <= score <= 100:
        A+=1
    elif 80 <= score <= 90:
        B+=1
    elif 70 <= score <= 80:
        C+=1
    elif 60 <= score <= 70:
        D+=1
    else:
        F+=1
print("A: {}\nB: {}\nC: {}\nD: {}\nF: {}".format(A,B,C,D,F))