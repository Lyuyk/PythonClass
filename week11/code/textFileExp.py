"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：textFileExp.py
@time:2022/5/5上午 8:35
@function:实现文本文件读取，第一步：打开文件，第二部：读取数据，第三步：关闭文件
"""

# 两个点出去
file1=open("../dataset/test.txt","rt")
#file2=open(".../week11/dataset/test.")
print(type(file1))

content=file1.read()
print(type(content))
print(content)

file1.seek(0) #将文件指针指向文件开始（读第二次需要的操作）
content=file1.read()
print(content)

file1.seek(0)
content=file1.readlines() #readline()读1行，readlines()都所有行，并以列表的方式返回
content1=[line.replace('\n','') for line in content] #去掉了'\n'
print(content1)

file1.close()

