"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp2Bmain_2pointsDistance.py
@time:2022/5/15下午 10:05

"""
import Exp2B_2pointsDistance

if __name__=="__main__":
    #point1=list(map(int,list(input().split(' '))))
    #point2=list(map(int,list(input().split(' '))))
    list=Exp2B_2pointsDistance.enterDis(*(list(map(int,list(input("输入两点坐标以空格间开").split(' '))))))
    print("两点间横向距离为：{}，空间距离为{}".format(list[0],list[1]))
    #print(Exp2B_2pointsDistance.distance(1, 1, 1, 2, 2, 2))