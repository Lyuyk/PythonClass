"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：C4C.py
@time:2022/4/10上午 10:39

"""


t = eval(input())
for i in range(t):
    n = eval(input())
    l = list()
    for i in range(n):
        sname, d, t = input().split()
        l.append([str(sname), int(d), int(t)])
    l = sorted(l, key=lambda x: (-x[1], -x[2], x[0]), reverse=False)
    flag1, flag2 = 0, 0
    ls1, ls2 = 0, 0
    for x in range(n):
        flag2 += 1
        if ls1 == l[x][1] and ls2 == l[x][2]:
            flag1 = flag1
        else:
            ls1, ls2 = l[x][1], l[x][2]
            flag1 = flag2
        print(flag1, ' '.join(str(i) for i in l[x]))