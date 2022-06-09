# -*- coding: utf-8 -*-

"""
    作者:     Zc
    版本:     1.0
    日期:     2020/04
    文件名:    main.py
    功能：     主程序

    实战案例1-1：课程成绩数据分析 (1)
    任务：
        - 学生成绩统计
        - 分析专业、课程的学生成绩数据

    数据集来源：略

"""
import csv
import os
import numpy as np

# 指定数据集路径
dataset_path = './data'

# 结果保存路径
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)
    

def load_data(data_file, usecols):
    """
        读取数据文件，加载数据
        参数：
            - data_file:    文件路径
            - usecols:      所使用的列
        返回：
            - data_arr:     数据的多维数组表示
    """
    data = []
    with open(data_file, 'r') as csvfile:
        data_reader = csv.DictReader(csvfile)
        # === Step 2. 数据处理 ===
        for row in data_reader:
            # 取出每行数据，组合为一个列表放入数据列表中
            row_data = []
            # 注意csv模块读入的数据全部为字符串类型
            for col in usecols:
                str_val = row[col]
                # 数据类型转换为float，如果是'NA'，则返回nan
                row_data.append(float(str_val) if str_val != 'NA' else np.nan)

            # 如果行数据中不包含nan才保存该行记录
            if not any(np.isnan(row_data)):
                data.append(row_data)

    # 将data转换为ndarray
    data_arr = np.array(data)
    return data_arr

def get_score_distribute(data):
    """
    返回 优秀、良好、中等、几个、不及格 比率
        规则：
        优秀                90 <= Score <= 100
        良好                80 <= Score < 90
        中等                70 <= Score < 80
        及格                60 <= Score < 70
        不及格              Score < 60
    """
    total = len(data)
    excellent = data[data >= 90].shape[0]
    good = data[(data >= 80) & (data < 90)].shape[0]
    medium = data[(data >= 70) & (data < 80)].shape[0]
    pass_ = data[(data >= 60) & (data < 70)].shape[0]
    fail = data[data < 60].shape[0]
    return excellent / total, good / total, medium / total, pass_ / total, fail / total


def get_student_score(data_arr):
    """
    获取学生成绩分布的统计数
    参数：
        - data_arr: 数据的多维数组表示
    返回：
        - student_socre: 学生成绩列表
        （No 学号, Major 专业, Avg 平均分, Total 参与课程数, Excellent 优秀率, Good 良好率, Medium 中等率, Pass 及格率, Fail 不及格率）
    """
    student_score = []
    # 获取学生列表
    student_list = np.unique(data_arr[:, 0])
    
    for student in student_list:
        score_list = data_arr[data_arr[:, 0] == student]
        avg = np.mean(score_list[:, 3])
        total = score_list.shape[0]
        major = score_list[0][1]
        # Excellent, Good, Medium, Pass, Fail 
        excellent, good, medium, pass_, fail = get_score_distribute(score_list[:, 3])
        score = [int(student), int(major), avg, int(total), excellent, good, medium, pass_, fail]
        student_score.append(score)
    # 按平均分排序
    student_score = np.array(sorted(student_score, key = lambda x : x[2], reverse=True))
    return student_score


def get_major_score(student_score):
    """
    统计专业平均分数分布
    参数：
        - data_arr: 数据的多维数组表示
    返回：
        - major_score:  多维数组结果
        （Course, Total, Excellent, Good, Medium, Pass, Fail ）
    """
    major_score = []
    # 获取专业列表
    major_list = np.unique(student_score[:, 1])
    for major in major_list:
        score_list = student_score[student_score[:, 1] == major]
        total = score_list.shape[0]
        excellent, good, medium, pass_, fail = get_score_distribute(score_list[:, 2])
        major_score.append([major, total, excellent, good, medium, pass_, fail])
    
    return np.array(major_score)

def get_course_score(data_arr):
    """
    统计课程分数分布
    参数：
        - data_arr: 学生成绩
    返回：
        - major_score:  多维数组结果
        （Course, Avg, Total, Excellent, Good, Medium, Pass, Fail ）
    """
    course_score = []
    # 获取课程列表
    course_list = np.unique(data_arr[:, 2])
    for course in course_list:
        score_list = data_arr[data_arr[:, 2] == course]
        avg = np.mean(score_list[:, 3])
        total = score_list.shape[0]
        excellent, good, medium, pass_, fail = get_score_distribute(score_list[:, 3])
        score = [int(course), avg, int(total), excellent, good, medium, pass_, fail]
        course_score.append(score)
    # 按平均分排序
    course_score = np.array(sorted(course_score, key = lambda x : x[1], reverse=True))
    return course_score
    
def save_to_csv(data, save_file, headers):
    """
        将统计结果保存至csv文件中
        参数：
            - data:   多维数组结果
            - file_name:    文件明
            - headers:      csv表头
    """
    with open(save_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data.tolist():
            writer.writerow(row)



def main():
    """
        主函数
    """
    colleges = ['cs']

    for college in colleges:
        # === Step 1+2. 数据获取 + 数据处理 ===
        file_name = college + '.csv'
        data_file = os.path.join(dataset_path, file_name)
        
        cols = [ 'No', 'Major', 'Course', 'Score']
        data_arr = load_data(data_file, cols)

        print('{}共有{}行有效数据'.format(college, data_arr.shape[0]))
        # 预览前10行数据
        print('{}的前10行数据：'.format(college))
        print(data_arr[:10])

        # === Step 3. 数据分析 ===
        # 学生维度 成绩分析
        student_score_info = get_student_score(data_arr)
        # print(student_score_info)
        # 专业维度 成绩分析
        major_score_info = get_major_score(student_score_info)
        # print(major_score_info)
        # 课程维度 成绩分析
        course_score_into = get_course_score(data_arr) 
        # print(course_score_into)
        
        # === Step 4. 结果保存 ===     
        save_to_csv(data = student_score_info, 
             save_file = os.path.join(output_path, 'student_score_info.csv'), 
             headers = ['No', 'Major', 'Avg', 'Total', 'Excellent', 'Good', 'Medium', 'Pass', 'Fail'])
        print('student_score_info.csv 保存成功')
        save_to_csv(data = major_score_info, 
             save_file = os.path.join(output_path, 'major_score_info.csv'), 
             headers = ['Major', 'Total', 'Excellent', 'Good', 'Medium', 'Pass', 'Fail'])
        print('major_score_info.csv 保存成功')
        save_to_csv(data = course_score_into, 
             save_file = os.path.join(output_path, 'course_score_info.csv'), 
             headers = ['Course', 'Avg', 'Total', 'Excellent', 'Good', 'Medium', 'Pass', 'Fail'])
        print('course_score_info.csv 保存成功')
if __name__ == '__main__':
    main()
