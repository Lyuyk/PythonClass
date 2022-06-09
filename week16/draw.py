"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：draw.py
@time:2022/6/9上午 8:34
@function: 画一个多图
"""

import matplotlib.pyplot as plt
import numpy as np

#任务1 得到画布
fig = plt.figure()

ax1 = plt.subplot(221) #得到一个坐标轴，放置在画布2行2列第一个位置

#任务2 准备数据

x = np.linspace(-2*np.pi,2*np.pi,50)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,'r-.')
plt.plot(x,z,'g--')

#任务3 对图形进行装饰
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('sin function visualization')

ax2 = plt.subplot(222)
x1 = [10 + np.random.randn() for i in range(50)]
y1 = [20 + np.random.randn() for i in range(50)]

x2 = [15 + np.random.randn() for i in range(50)]
y2 = [30 + np.random.randn() for i in range(50)]
plt.scatter(x1,y1) #实现散点图
plt.scatter(x2,y2)


#任务4 显示图像
plt.show()