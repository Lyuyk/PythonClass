"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp3A_jsonNcsv.py
@time:2022/5/18下午 9:34
@function:
"""
import csv
import json #导入第三方库json
import pprint
import random

def loadDataFromJson(filePath):
    with open(filePath,'r',encoding='utf-8') as f: # with 上下文管理器（辅助关闭文件，处理错误）
        cityList = json.load(f) # 使用了json模块的load方法装入json文件内容
    return cityList

def jsonTocsv(filePath):
    data = loadDataFromJson(filePath)
    headlist=[i for i in data[0].keys()] #表头
    csv_data=[]#要写入csv的列表内容
    csv_data.append(headlist)

    data_list=[]
    #每次循环写入一列
    for j in range(len(data)):
        data_list.append([i for i in data[j].values()])
    #升序排列
    data_list.sort(key=lambda x:x[0])
    #内容写入csv列表中
    for i in data_list:
        csv_data.append(i)
    return csv_data

#写回到csv文件中
def writeToCsv(filePath,csvData):
    with open(filePath, "w", encoding="utf-8", newline='') as wt:
        csvW = csv.writer(wt)
        for line in csvData:
            csvW.writerow(line)

if __name__=="__main__":
    filePath="./src/beijing_aqi.json"
    csvPath="./src/beijing_aqi.csv"
    csv_data = jsonTocsv(filePath)#加载得到的json文件并排序返回为csv文件
    writeToCsv(csvPath,csv_data)#写入csv文件中
