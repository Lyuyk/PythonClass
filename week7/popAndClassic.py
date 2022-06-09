"""
程序功能：实现流行电影与经典电影的操作
"""

#任务1：描述正在播放流行电影
popMovie1 = ['长津湖','狙击手','中国机长','误杀','中国机长','中国机长']
popMovie = {'长津湖','狙击手','中国机长','误杀','中国机长','中国机长'}
print(len(popMovie1))
print(len(popMovie))

#任务2：向流行电影中增加新的流行电影
popMovie.add('蜘蛛侠')
popMovie.add('泰坦尼克号')
print('流行电影有：',popMovie)


#任务3：描述正在播放的经典电影
classicMovie = {'蜘蛛侠','肖申克的救赎','阿甘正传'}
print('经典电影有：',classicMovie)


#任务4：既流行，又经典的电影
print('既流行，又经典的电影',popMovie.intersection(classicMovie))
print(popMovie)
print(classicMovie)

#print('既流行，又经典的电影2',popMovie.intersection_update(classicMovie))
#print(popMovie)
#print(classicMovie)

#任务5：找出流行但不是经典的电影
print('找出流行但不是经典的电影',popMovie-classicMovie)
print('找出流行但不是经典的电影2',popMovie.difference(classicMovie))

#任务6：找出流行或者经典的电影
print('流行或者经典的电影',popMovie | classicMovie)
print('流行或者经典的电影2',popMovie.union(classicMovie))

#任务7：增减流行或经典电影
popMovie.add('星球大战')
print(classicMovie.pop())



