"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：C4A.py
@time:2022/4/6下午 10:18

"""

polynomial1=(input().split(','))
polynomial2=(input().split(','))
aim=int(input())
plist=[]
dict_list={}
for i in polynomial1:
    plist.append([int(j) for j in str(i).split()])


dict_list=dict(plist)
dict_list=dict(zip(dict_list.values(),dict_list.keys()))
plist.clear()

for i in polynomial2:
    ilist = [int(j) for j in str(i).split()]
    if(ilist[1] in dict_list.keys()):
        dict_list[ilist[1]]+=ilist[0]
    else:
        plist.append(ilist)

dit=dict(plist)
dit_inv=dict(zip(dit.values(),dit.keys()))
dict_list.update(dit)




#print(polynomial1)
#print(polynomial2)
#print(dict_list)
print(dict_list[aim])
