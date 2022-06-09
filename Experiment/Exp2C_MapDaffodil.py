"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp2C_MapDaffodil.py
@time:2022/5/12下午 5:03
@function:利用高阶函数map求解所有3位4位5位水仙花数
"""

#准备数字列表
numlist=[str(num) for num in range(100,99999)]
#存水仙花数的空列表
daffodil=[]

for strr in numlist:
    num=int(strr)
    nlist=list(map(int,strr))#各位数分开存成一个列表
    level=len(nlist)#确定要乘的列数

    #计算要求的各个位数幂的和
    sum=0
    for i in range(len(nlist)):
        sum+=pow(nlist[i],level)
    #若相等则加入水仙花数列表中
    if sum==num:
        daffodil.append(num)

print("水仙花数有：",daffodil)