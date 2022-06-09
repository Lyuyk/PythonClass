"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp3C_txtTocsv.py
@time:2022/5/18下午 9:37

"""
"""
soup=BeautifulSoup(open('./src/Dylan_van_Baarle.txt',encoding='utf-8'),features='html.parser')
#print(soup)
soupSet=soup.find_all('script' ,type="text/javascript", string=re.compile("Dylan van Baarle"))
#re_data=re.search(r'\{"userName"^[\s\S]*\"swimLengthList":null}}$')^\\[{"userName][\s\S]*
strr=str(soupSet)
str_data=re.findall(r'\\[swimLengthList":null}}]$',strr)
print(str_data)
"""

import csv
import re

reg = re.compile(r'[\[0-9]\d*.\d*,[0-9]\d*.\d*,[0-9]\d*.\d*,[0-9]\d*.\d*,[0-9]\d*.\d*,[0-9]\d*.\d*,[0-9]\d*.\d*,[0-9]\d*.\d*,[0-9]\d*.\d*]')
with open("./src/Dylan_van_Baarle.txt", encoding="utf-8") as file:
    ans = []
    for line in file:
        #正则匹配
        m = reg.findall(line)
        #若匹配得到的数据非空则加入
        if m is not None and m != []:
            ans += m

#print(ans)

with open("./src/train_DvB.csv", "w", encoding="utf-8", newline="") as fw:
    csvWriter = csv.writer(fw)
    csvWriter.writerow(
        ['ms', 'speed', 'elevation', 'temperature', 'cadence', 'power', 'distance', 'positionLat', 'positionLong'])
    for lst in ans:
        #再次匹配，因为之前得到的ans数据得到的每元素都是每一行数据组成的字符串，匹配以分开
        data = re.findall("[0-9]\d*.\d*", lst)
        #print(data)
        csvWriter.writerow(data)

