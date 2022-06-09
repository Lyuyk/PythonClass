import csv

import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
    'Referer': 'http://fundf10.eastmoney.com/jjjz_160706.html'
}
def get_html(url,csvlist):
    html = requests.get(url,headers=headers)
    html_text= html.text
    print(html_text)
    start = html_text.find('{"Data":{"LSJZList"')
    json_data = json.loads(html_text[start:-1])
    netvalues = json_data['Data']['LSJZList']
    for data in netvalues:
        fsrq = data['FSRQ'] #发生日期
        dwjz = data['DWJZ'] #单位净值
        ljjz = data['LJJZ'] #累计净值
        jzzzl = data['JZZZL'] #净值增长率
        csvlist.append([fsrq,dwjz,ljjz,jzzzl])
        print(fsrq,dwjz,ljjz,jzzzl) #找到并显示输出
    #print(csvlist)
    return csvlist


def writeToCsv(filePath,csvData):
    with open(filePath, "w", encoding="utf-8", newline='') as wt:
        csvW = csv.writer(wt)
        for line in csvData:
            csvW.writerow(line)

if __name__ == '__main__':
    csvlist = [["发生日期", "单位净值", "累计净值", "净值增长率"]]
    for i in range(1,11):
        url = 'http://api.fund.eastmoney.com/f10/lsjz?' \
              'callback=jQuery183015088915834593553_1586246635664&' \
              'fundCode=160706&pageIndex={}&pageSize=20&' \
              'startDate=&endDate=&_=1586246635678'.format(i)
        print('当前输出地{}页'.format(i))
        get_html(url,csvlist)
    writeToCsv("./src/HS300.csv", csvlist)