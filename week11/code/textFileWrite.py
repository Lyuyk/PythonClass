"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：textFileWrite.py
@time:2022/5/5上午 8:50
@function:实现文本文件读取，第一步：打开文件，第二部：写入数据，第三步：关闭文件
"""

fileName = input("请输入一个文件名：")

file2 = open('../dataset/'+fileName,'wt') #write text file

print(type(file2))

alist=['hello everyone','大家好','我爱你们']

alist1 ='\n'.join(alist) # 列表中元素以'\n'连接
print(alist1)

file2.writelines(alist1)

file2.close()
