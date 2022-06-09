'''
已经建立文本文件abc.txt，编写一个程序，统计并输出文件中元音字母出现的次数。

---------------------------------------------------------------------------
输入格式:
数据格式见abc.txt

输出格式:
元音字母出现的?次
---------------------------------------------------------------------------
输入样例1:
见abc.txt
输出样例1:
元音字母出现的191次
-----------------------------------------------------------------
以上是题目，不要更改，从下面开始答题！！！
'''

with open('abc.txt','r') as f:
    text=f.read()
charList="aeiouAEIOU"
sum=0
for i in text:
    if i in charList:
        sum+=1
print("元音字母出现的{}次".format(sum))
        
        
