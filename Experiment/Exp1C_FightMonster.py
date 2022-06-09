"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp1C_FightMonster.py
@time:2022/4/27下午 11:40
@title:假设有一个玩家，一个怪物，分别对应一连串数字，第一个数字为初始血量，从第二个开始到最后为其可能的攻击力，
        可选择的攻击力数量大于等于2， 每回合都有可能是玩家或者怪物攻击（随机选择），攻
        击力为玩家/怪物本身的攻击力中的随机一个，互相攻击直到其中一方血量小于等于0，输出胜利者及其剩余血量

"""
import random

#假设一个玩家，一个怪物，分别对应一串数字，典型的Key：Value，用字典，Value为list
#1:初始血量 2~x：可能攻击力
#生成随机资料
role = {"player": [random.randint(40,100) for i in range(random.randint(2, 10))], "monster": [random.randint(40,100) for j in range(random.randint(2, 10))]}
#直到一方血量小于等于0，外层套一个while循环    #每回合都选择一个角色随机攻击，攻击力随机选择，用random
while role["player"][0] > 0 and role["monster"][0] > 0:
    n = random.randint(1, 2)
    if n == 1:#player 攻击
        choice = random.randint(1, len(role["player"])-1) # 在范围内选择招数
        role["monster"][0] -= role["player"][choice] #减去伤害
    else:
        choice = random.randint(1, len(role["monster"])-1) # 在范围内选择招数
        role["player"][0] -= role["monster"][choice] #减去伤害

if role["player"][0] > 0:
    print('player win!')
else:
    print('monster win!')
