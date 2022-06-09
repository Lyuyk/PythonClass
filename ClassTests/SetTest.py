"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：SetTest.py
@time:2022/4/10下午 5:01

"""
import time

start = time.time()
int('1'*11164, 2)
end = time.time()
print(end-start)


start = time.time()
sum(2**i for i in range(11164))
end = time.time()
print(end-start)

