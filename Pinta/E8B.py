"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E8B.py
@time:2022/6/1下午 7:45

"""
import math


class Rect :
    def __init__(self, l, h, z) :
        self.l = l
        self.h = h
        self.z = z

    def lenght(self) :
        return 2 * (self.l + self.h)

    def area(self) :
        return self.l * self.h


class Cubic(Rect) :
    def __init__(self, l, h, z) :
        super(Cubic, self).__init__(l, h, z)

    def v(self) :
        return self.l * self.h * self.z

    def area(self) :
        return 2 * (self.l * self.h + self.l * self.z + self.z * self.h)


class Pyramid(Rect) :
    def __init__(self, l, h, z) :
        super(Pyramid, self).__init__(l, h, z)

    def v(self) :
        return self.l * self.z * self.h / 3

    def area(self):
        return math.sqrt(self.h*self.h+4*self.z*self.z)*self.l/2+self.h*self.l+math.sqrt(self.l*self.l+4*self.z*self.z)*self.h/2

while True:
    try:
        l,h,z=map(float,input().split())
        for i in range(4):
            if l<=0 or h<=0 or z<=0:
                print("0.00 0.00 0.00 0.00")
                break
            else:
                if i==0:
                    print("%.2f"%Cubic(l,h,z).area(),end=" ")
                elif i==1:
                    print("%.2f"%Cubic(l,h,z).v(),end=" ")
                elif i==2:
                    print("%.2f" % Pyramid(l, h, z).area(), end=" ")
                elif i==3:
                    print("%.2f" % Pyramid(l, h, z).v())
    except:
        break