"""
    功能：读取空气质量指数的JSON文件（beijing_aqi.json），按aqi排序，并将前5个写到JSON文件（top5_aqi.json）中
    作者：张三
    版本：1.0
    日期：3/15/2022
"""
import json

def process_json_file(filepath):
    # 任务1：读取并解码json文件
    pass

    return city_list

def main():
    # 主函数
    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    # 按aqi排序并取前5个
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]

    # 任务2：将aqi前5个写到JSON文件（top5_aqi.json）
    pass


if __name__ == '__main__':
    main()
