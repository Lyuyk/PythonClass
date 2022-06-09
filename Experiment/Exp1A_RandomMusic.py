"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp1A_RandomMusic.py
@time:2022/4/27下午 10:13
@title:两类音乐分别存储在文件夹happy和sad中
       用户输入心情（0代表开心，1代表伤心，8代表不想听了），系统根据随机选取音乐播放100秒
"""

import pygame
import os
from random import randint


# path音乐路径，sleeptime持续时间
def playM(path, time):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    time.sleep(time)


happy_list = [filename for filename in (os.listdir('.\music\happy')) if filename[-3:] == 'mp3']
sad_list = [filename for filename in (os.listdir('.\music\sad')) if filename[-3:] == 'mp3']
path_list = ['.\music\happy\\', '.\music\sad\\']

# 用户输入心情（0代表开心，1代表伤心，8代表不想听了），系统根据随机选取音乐播放100秒
while (True):
    feeling = int(input("请输入心情（0代表开心，1代表伤心，8代表不想听了）："))
    if (feeling == 0):
        playM(path_list[feeling] + happy_list[randint(0, len(happy_list) - 1)], 10)
    elif (feeling == 1):
        playM(path_list[feeling] + sad_list[randint(0, len(sad_list) - 1)], 10)
    elif (feeling == 8):
        print('See u soon!')
        break
