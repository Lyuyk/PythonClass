"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：test.py
@time:2022/6/1下午 8:02


preList=[]
resList=[]

with open('data.txt','r') as f:
    lines=f.readlines()
    for word in lines:
        word=word.strip()
        preList.append(len(word))
    maxLength=max(preList)
    for word in lines:
        if len(word.strip()) == maxLength:
            resList.append(word)

with open('result.txt','w') as w:
    if len(resList) == 1:
        w.write("The longest word is: {0}".format(resList[0]))
    else:
        resultList=','.join(resList)
        w.write("The longest words are: {0}".format(resultList))
"""
a = []
b = []
c = []
with open('data.txt', 'r') as fp :  # 读取文本文件文件
    txt = fp.readlines()  # 把文本文件中的每行文件作为一个字符串存入txt列表中
    for i in range(len(txt)) :
        txt[i] = txt[i].strip()  # 删除当前字符串两端的空白字符
        a.append(len(txt[i]))  # 将删除空白字符后的字符串追加到列表a中
    for i in txt :
        if i != '' :
            b.append(i)  # 若字符串不为空则将其存放到列表b中
    m = b[0]
    for i in b :
        if len(i) > len(m) :
            m = i
    n = len(m)  # 遍历查找列表中的最长元素
    for i in b :
        if len(i) == n :
            c.append(i)  # 遍历查找所有与最长元素等长的字符串，将所有合法
            # 字符串存入列表c中

with open('result.txt', 'w') as fp :
    if len(c) == 1 :
        fp.write('The longest word is: {0}'.format(c[0]))  # 满足条件的字符串只有一个
    else :
        d = ','.join(c)
        fp.write('The longest words are: {0}'.format(d))  # 满足条件的字符串有多个