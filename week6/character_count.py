"""
    功能：生成1000个随机字符的字符串，然后统计每个字符的出现次数
    作者：张三
    版本：1.0
    日期：3/15/2022
"""

import string
import random

random.seed(88)
# 产生可选字符
x = string.ascii_letters + string.digits + string.punctuation
# 任务1：生成1000个随机字符的字符串
alist = [random.choice(x) for i in range(1000)]

# 任务2：利用字典统计每个字符的出现次数
d = dict()  # 存放字符及频度
for ch in alist:
    d[ch] = d.get(ch, 0) + 1
print(d)

# 任务3：排序并输出出现频率最高的前十个字符
orderD=sorted(d.items(),key=lambda x : x[1],reverse=True)#d.items()排序的是每一个键值对，lambda x:x[1]排序根据为值
print(orderD[0:10])
top10=orderD[0:10]#切片
print('频率最高的前十个字符及出现频率为',top10)
top10Char=[item[0] for item in top10]
print(top10Char)

blist=['a','b','c','d']
dd = dict()
for char in blist:
    dd[char] = dd.get(char, 0)+1
print(dd)
