"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：E5A.py
@time:2022/6/1上午 10:33

"""

dic = {'admin': '123456', 'administrator': '12345678', 'root': 'password'}
logining = True
while logining:
    try:
        for i in range(3):
            username = input()
            password = input()
            if username in dic.keys():
                if dic[username] == password:
                    print("登录成功", end='')
                    logining = False
                    break
                else:
                    print("登录失败")
            else:
                print("登录失败")
        logining = False
    except EOFError:
        pass



