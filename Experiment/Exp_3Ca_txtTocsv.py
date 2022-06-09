"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：Exp_3Ca_txtTocsv.py
@time:2022/5/26下午 3:48

"""

import json
import csv
with open("./src/Dylan_van_Baarle.txt",'r',encoding='utf-8') as f:
    raw_data=''
    linenum=0
    for line in f:
        if 'var publicActivityWrapper = ' in line:
            raw_data=line
            break
    raw_data=raw_data.replace('var publicActivityWrapper = ','')[:-2]
    data=json.loads(raw_data)

with open('./src/train_DvB_temp.json','w') as f:
    f.write(json.dumps(data,indent=4))

data=data['workoutDetailData']['workoutSampleList']
key=data['channelSet']

with open('./src/train_DvB.csv','w',newline='') as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(['ms']+key[1:])#写入表头
    #print(['ms']+key[1:])
    #写入数据本体
    for dt in data['samples']:
        datalist=dt['values'][1:]
        datalist.insert(0,dt['ms'])
        csvWriter.writerow(datalist)
        #dt['values']
        #dt['ms']
        #print(datalist)