"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E7C.py
@time:2022/5/26上午 9:14

"""

strr=input()
#编写一个函数，判断输入的字符串是否由小写字母和数字组成
length = len(strr)
a = 0     #用于记录在ASCII码内并累加，最后和字符串长度一致则认为是以下结论
b = 0
for i in strr :
    num = ord(i)    #ord（）把字符串转为ASCII码
    if 48 <= num <= 57 :   # 对应ASCII码的数字值
        a += 1      #在范围内就累加
    if 97 <= num <= 122:   # 对应ASCII码的小写字母
        b += 1
c = a + b
if c == length :       #判断累加结果与字符串长度
    print("该字符串由小写字母和数字组成")
else:
    print("该字符串不是由小写字母和数字组成！")