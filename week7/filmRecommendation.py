"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：filmRecommendation.py
@time:2022/4/7上午 9:56

"""
from pprint import pprint
import random
"""
10user,5films,score1-10
"""



movieData = {'user' + str(i): {'film' + str(random.randrange(1, 6)): random.randrange(1, 11) for j in
                               range(random.randrange(3, 6))} for i in range(1, 11)}

pprint(movieData)

#当前用户
user={'film'+str(random.randrange(1,6)):random.randrange(1,10)for i in range(5)}
print('当前用户是：',user)

#'user':{'film2': 1, 'film5': 8, 'film3': 7, 'film1': 1}->{'film2': 1, 'film5': 8, 'film3': 7, 'film1': 1}->{'film1','film3','film5'} tuple->dict->dict
similarUser,films=min(movieData.items(),key=lambda item:(-len(item[1].keys()&user.keys()),
                                    sum(((item[1].get(film)-user.get(film)) ** 2 for film in user.keys() & item[1].keys()))))#负 越多越小


print('known data'.center(50,'*'))
#for item in movieData.items():
 #  print(len(item[1].keys & user.keys()),sum(((item[1].get(film)-user.get(film))**2 for film in user.keys() & item[1].keys())),item,sep=':')
print('current user'.center(50,'*'))
print(user)
print('most similar user and his films'.center(50,'*'))
print(similarUser)

#没看过的电影中选择打分最高进行排行
print('recommended films'.center(50,'*'))
print(max(films.keys()-user.keys(),key=lambda film:films[film]))