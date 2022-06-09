"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E5B.py
@time:2022/6/1上午 11:22

"""

dictA=dict(eval(input()))
dictB=dict(eval(input()))
dictC= {}

for key1, val1 in dictA.items():
    for key2, val2 in dictB.items():
        if key1==key2:
            dictC[key1]=int(val1)+int(val2)
        if key1 not in dictC:
            dictC[key1]=val1
        if key2 not in dictC:
            dictC[key2]=val2

dictC=dict(sorted(dictC.items(),key=lambda x:x[0] if type(x[0]) == int else ord(x[0])))

print(str(dictC).replace(' ', '').replace("'",'"'))