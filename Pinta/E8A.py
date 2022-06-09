"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E8A.py
@time:2022/5/26上午 9:38

"""

class VecCal():
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, n):
        result = VecCal()
        result.x=self.x + n.x
        result.y=self.y + n.y
        result.z=self.z + n.z
        return result

    def __sub__(self, n) :  # 定义向量的减法运算
        result = VecCal()
        result.x=self.x - n.x
        result.y=self.y - n.y
        result.z=self.z - n.z
        return result

    def __mul__(self, i) :  # 定义向量的乘法运算
        result = VecCal()
        result.x=self.x * i
        result.y=self.y * i
        result.z=self.z * i
        return result

    def __div__(self, i) :  # 定义向量的除法运算
        if i==0:
            return VecCal()
        result = VecCal()
        result.x=self.x // i
        result.y=self.y // i
        result.z=self.z // i
        return result

    def show(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)


VecAlist=list(map(int,input().split(',')))
VecA=VecCal(VecAlist[0],VecAlist[1],VecAlist[2])




VecBlist=list(map(int,input().split(',')))
VecB=VecCal(VecBlist[0],VecBlist[1],VecBlist[2])
VecAdd=VecA.__add__(VecB)
VecSub=VecA.__sub__(VecB)
num=int(input())
VecMlt=VecA.__mul__(num)
VecDiv=VecA.__div__(num)
print("({}, {}, {}) + ({}, {}, {}) = {}".format(VecAlist[0],VecAlist[1],VecAlist[2],VecBlist[0],VecBlist[1],VecBlist[2],VecAdd.show()))
print("({}, {}, {}) - ({},{},{}) = {}".format(VecAlist[0],VecAlist[1],VecAlist[2],VecBlist[0],VecBlist[1],VecBlist[2],VecSub.show()))
print("({}, {}, {}) * {} = {}".format(VecAlist[0],VecAlist[1],VecAlist[2],num,VecMlt.show()))
print("({}, {}, {}) / {} = {}".format(VecAlist[0],VecAlist[1],VecAlist[2],num,VecDiv.show()))



