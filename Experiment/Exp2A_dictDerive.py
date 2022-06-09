"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp2A_dictDerive.py
@time:2022/5/12下午 4:30
@function:用字典推导式产生40个学生的学号及语文、数学、英语成绩（成绩随机产生，范围在50-150之间）

"""
import random

#用字典推导式产生40个学生的学号及语文、数学、英语成绩（成绩随机产生，范围在50-150之间）
#score_list={str("学号:"+str(i)):{"语文":random.randint(50,150),"数学":random.randint(50,150),"英语":random.randint(50,150)} for i in range(202001,202041)}
score_list={str("学号:"+str(i)): dict(语文=random.randint(50, 150), 数学=random.randint(50, 150), 英语=random.randint(50, 150))
            for i in range(202001, 202041)}#不包括2020041
    #score_list[str("学号:"+str(i))]=scores

print(score_list)
#print(len(score_list))

#添加总分关键字及总分
for s in score_list.values():
    #print(s)
    Sum=0
    for i in s.values():
        Sum+=i
    s["总分"]=Sum
    print(s)

#按总分由高到低排序
list=[]
for i in score_list.items():
    print(i)
    list.append(i)

list.sort(key=lambda x:x[1]["总分"],reverse=True)
print(list)