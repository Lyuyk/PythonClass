"""
    作者：张三
    功能：将列表中的成绩数据写入scores.json文件，转换并写入规范的csv文件（scores.csv）
    版本：1.0
    日期：05/15/2022
"""
import json
import csv

# 列表scores中存储了10个学生的成绩
scores = [('学号:201801', {'语文': 148, '数学': 141, '英语': 68, '总分': 357}),
          ('学号:201803', {'语文': 140, '数学': 79, '英语': 85, '总分': 304}),
          ('学号:201807', {'语文': 146, '数学': 101, '英语': 57, '总分': 304}),
          ('学号:201809', {'语文': 119, '数学': 106, '英语': 69, '总分': 294}),
          ('学号:201804', {'语文': 101, '数学': 106, '英语': 78, '总分': 285}),
          ('学号:201808', {'语文': 100, '数学': 102, '英语': 74, '总分': 276}),
          ('学号:201805', {'语文': 127, '数学': 76, '英语': 70, '总分': 273}),
          ('学号:201802', {'语文': 113, '数学': 62, '英语': 80, '总分': 255}),
          ('学号:201806', {'语文': 76, '数学': 94, '英语': 70, '总分': 240})]

# 任务1：将列表中的成绩数据写入scores.json文件


with open("../dataset/scores.json", "w", encoding='utf-8') as fp:
    json.dump(scores, fp, ensure_ascii=False, indent=4)

# 任务2: 将列表中的成绩数据转换并写入规范的csv文件（scores.csv）
# 格式为：学号,语文,数学,英语,总分
#         201805,147,101,76,324
#         201809,93,145,53,291
with open("../dataset/scores.json", "r", encoding='utf-8') as jsn:
    scoreList = json.load(jsn)

data = []
dataHead = scores[0][0][0:2]#学号字段
data.append(dataHead)#添加学号字段
data.extend(list(scores[0][1].keys()))#csv表头
print(data)

csvData=[]
for dat in scores:
    sno= dat[0][3:]#学号
    score = list(dat[1].values())
    score.insert(0,sno)
    csvData.append(score)

csvData.insert(0,data)#添加表头
print(csvData)


with open("../dataset/scores.csv","w",encoding="utf-8",newline='') as wt:
    csvW=csv.writer(wt)
    for line in csvData:
        csvW.writerow(line)


