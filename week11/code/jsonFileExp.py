"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：jsonFileExp.py
@time:2022/5/5上午 9:07
@function: 实现json数据文件读写操作
"""

import json #导入第三方库json
import pprint
import random

# 仅加载json数据
def loadDataFromJson(filePath):
    with open(filePath,'r',encoding='utf-8') as f: # with 上下文管理器（辅助关闭文件，处理错误）
        cityList = json.load(f) # 使用了json模块的load方法装入json文件内容
    return cityList

# 仅写入json数据
def dumpJsonData(filePath,data):
    with open(filePath,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=4) # 禁用ascii编码（py支持的是utf-8），缩进为4

# 加载并输出json数据
def loadPrintJson(filePath):
    data = loadDataFromJson(filePath)
    print(len(data))
    pprint.pprint(data[random.randint(1, len(data))])  # 随便print一条
    print("==========分割线===============")

    # 找出空气质量指数前三的数据
    sortedData = sorted(data, key=lambda x: x["aqi"])
    pprint.pprint(sortedData[0:3])
    return sortedData

if __name__=="__main__":
    filePath="../dataset/beijing_aqi.json"
    sortData = loadPrintJson(filePath)

    dumpJsonData('../dataset/beijing_aqi_top3.json',sortData[0:3])

