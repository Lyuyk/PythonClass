"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software: pycharm
@fileName: investment.py
@time: 2022/4/21上午 8:53
@function: 描述一个投资达人

"""

class InvestPerson:
    def __init__(self,name,age,sex,initMoney):
        self.name = name
        self.age = age
        self.sex = sex
        self.initMoney = initMoney

    def investStock(self,name,money,getMoney):
        self.initMoney = self.initMoney + 2000

    def investFunds(self):
        self.initMoney = self.initMoney + 1500

    def investDebt(self):
        self.initMoney = self.initMoney + 1000

liuxiaoxiao = InvestPerson('liuxiaoxiao',18,'女',1000)

print(liuxiaoxiao.name,liuxiaoxiao.sex,liuxiaoxiao.initMoney)
liuxiaoxiao.investFunds()
print(liuxiaoxiao.initMoney)

liuxiaoxiao.fuerDai = 5000000
print(liuxiaoxiao.fuerDai)
