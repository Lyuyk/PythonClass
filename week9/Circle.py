"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Circle.py
@time:2022/4/21上午 9:48

"""
import math
import pprint


class Circle:
    def __init__(self,radius):
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c=Circle(49)
print(c.radius)
print(c.area)
print(c.perimeter)

print(c.radius,c.area,c.perimeter)
