"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp1B_FruitOutOfWarehouse.py
@time:2022/4/27下午 11:38
@description: 有两个集合，一个表示商店当前包含的水果种类与个数，另一个表示仓库包含的水果种类，
                从仓库中随机取n次水果（每次取的个数为10以内随机数），n为仓库水果种类数的一半，如果仓库水果数为奇数则向下取整，
                仓库与商店中水果种类可能有重叠，但仓库与商店中的水果种类均不重复，输出最后商店中水果种类及其对应数量（按数量多少从小到大输出）。
"""

import random

# 两个集合，一个表示种类和个数，所以用字典，另一个列表和Set都可，但是仓库和商店中水果种类均不重复，这里采用Set
store = {"apple": 1, "banana": 2, "watermelon": 3}
stock = {"pear", "cherry", "apple", " orange"}

# 取水果数为仓库水果种类数的一半，用地板除获得次数，然后用choice进行随机选择  #取水果分为两种情况，原来有，那么数量追加，原来没有，则插入
for ep in range(len(stock) // 2):  # 拿种类数的一半次
    num = random.randint(1, 10)  # 拿n个
    choice = random.choice(list(stock))  # 挑一种水果拿1~10个
    store[choice]=store.get(choice,0)+num # 无则初始化，有则追加
# 排序并输出
sstore = sorted(store.items(), key=lambda x: x[1]) #使用键的值升序排列
print(sstore)
