"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Ex2.py
@time:2022/4/28上午 9:38

"""


from week10.ParaExample import *

if __name__=="__main__":
    """
    a=eval(input("input a:"))
    print(square(a))
    """
    print(Add(2,3,4,5))
    print(Add(2,3,4,5,6,7,8,9,10))
    print(Sum(2,3,z1=4,z2=5))

    print(Sum(2,3,z1=4,z2=5,z3=7,z4=8,z5=9,z6=10))
    myDict={"z1":4,"z2":5,"z3":7,"z4":8,"z5":9,"z6":10}
    print(Sum(2,3,**myDict))#加两星号传