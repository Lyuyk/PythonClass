"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E5D.py
@time:2022/6/1上午 11:49
@function:在某次竞赛中，判题规则是按解题数从多到少排序，在解题数相同的情况下，按总成绩（保证各不相同）从高到低排序，取排名前60%的参赛队（四舍五入取整）获奖，请确定某个队能否获奖。
"""

T=int(input())

for t in range(T):
    TeamAmount, guessTeam = input().split()
    TeamAmount=int(TeamAmount)
    awardIndex=int(TeamAmount*0.6+0.5)
    listS=[]
    listM=[]
    listG=[]
    list=[]
    for team in range(TeamAmount):
        s,m,g=input().split()
        m,g=int(m),int(g)
        listS.append(s)
        listM.append(m)
        listG.append(g)
    nameIndex=listS.index(guessTeam)
    grade=listG[nameIndex]

    listG.sort(reverse=True)
    sortedIndex=listG.index(grade)
    if sortedIndex<=awardIndex-1:
        print("YES")
    else:
        print("NO")
