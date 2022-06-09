"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E6B.py
@time:2022/6/1下午 4:14
@function:输入a,b班的名单，并进行如下统计。
输入格式:
第1行:：a班名单，一串字符串，每个字符代表一个学生，无空格，可能有重复字符。
第2行:：b班名单，一串字符串，每个学生名称以1个或多个空格分隔，可能有重复学生。
第3行:：参加acm竞赛的学生，一串字符串，每个学生名称以1个或多个空格分隔。
第4行：参加英语竞赛的学生，一串字符串，每个学生名称以1个或多个空格分隔。
第5行：转学的人(只有1个人)。
"""
import re
classAList=list(input())
classBList=re.split(r"[ ]+",input())
classAList,classBList=list(set(classAList)),list(set(classBList))

ACMRaceList=input().split()
englishRaceList=input().split()
transferStu=input()

total=list(set(classAList+classBList))
all_racers=list(set(ACMRaceList+englishRaceList))
not_in_race=list(set(total).difference(set(all_racers)))
acm_and_english=list(set(ACMRaceList).intersection(set(englishRaceList)))
acm_only=list(set(ACMRaceList).difference(set(englishRaceList)))
english_only=list(set(englishRaceList).difference(set(ACMRaceList)))
acm_or_english=list(acm_only+english_only)


print("Total:",len(total))
print("Not in race: {}, num: {}".format(sorted(not_in_race),len(not_in_race)))
print("All racers: {}, num: {}".format(sorted(all_racers),len(all_racers)))
print("ACM + English: {}, num: {}".format(sorted(acm_and_english),len(acm_and_english)))
print("Only ACM:",sorted(acm_only))
print("Only English:",sorted(english_only))
print("ACM Or English:",sorted(acm_only+english_only))

if transferStu in classAList:
    classAList.remove(transferStu)
    print(sorted(classAList))
elif transferStu in classBList:
    classBList.remove(transferStu)
    print(sorted(classBList))

