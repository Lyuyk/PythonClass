"""
    作者：张三
    功能：将存储成绩数据的csv文件（scores.csv）转换并写入scores.json文件
          csv格式为：学号,语文,数学,英语,总分
                     201805,147,101,76,324
                     201809,93,145,53,291
    版本：1.0
    日期：05/15/2022
"""
import json
import csv
# 任务1：利用csv库读取csv文件到列表scores_list
scores_list=[]
with open("../dataset/scores.csv","r",encoding='utf-8') as rf:
    csvR=csv.reader(rf)
    scores_list=list(csvR)
    #for line in csvR:
    #    scores_list.append(line)

print(scores_list)

# 任务2：转换并准备成列表嵌套字典scores_dict
scores_dict=[]
for i in range(1,len(scores_list)):# for i in scores_list[1:]:
    #dictA=dict(zip(scores_list[0][0],scores_list[0][0]))
    dictA={}
    dictA[scores_list[0][0]]= scores_list[i][0]#
    print(dictA)

    dictB=dict(zip(scores_list[0][1:],scores_list[i][1:]))
    print(dictB)

    dictA["成绩"]=dictB
    print(dictA)
    scores_dict.append(dictA)

    #scores_dict.append(dictA)
print(scores_dict)

# 任务3：将字典数据写入文件scores.json
with open("../dataset/scores(csv2json).json","w",encoding='utf-8') as jsn:
    json.dump(scores_dict,jsn,ensure_ascii=False,indent=4)



