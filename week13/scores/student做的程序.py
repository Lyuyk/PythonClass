"""
# Sample 1(按学生平均成绩排序)
# No, Avg, Total, Excellent, Good, Medium, Pass, Fail
# 学号，平均分，总课程数，优秀率，良好率，中等率，及格率，不及格率

# Sample 2（统计该专业各个平均分人数占比）
# Major, Total, Excellent, Good, Medium, Pass, Fail
# 专业，专业总人数，优秀率，良好率，中等率，及格率，不及格率

# Sample 3（统计课程各个平均分人数占比）
# Course, Avg, Total, Excellent, Good, Medium, Pass, Fail
# 课程，课程平均分，课程人数，优秀率，良好率，中等率，及格率，不及格率
"""
import numpy as np
import pandas as pd

# 创建dtype类型
student_dtype = np.dtype([('No', np.int), ('Avg', np.float), ('Total', np.int), ('Excellent', 'U6'),
                          ('Good', 'U6'), ('Medium', 'U6'), ('Pass', 'U6'), ('Fail', 'U6')])

Major_dtype = np.dtype([('Major', np.int), ('Total', np.int), ('Excellent', 'U6'),
                        ('Good', 'U6'), ('Medium', 'U6'), ('Pass', 'U6'), ('Fail', 'U6')])

Course_dtype = np.dtype([('Course', np.int), ('Avg', np.float), ('Total', np.int), ('Excellent', 'U6'),
                         ('Good', 'U6'), ('Medium', 'U6'), ('Pass', 'U6'), ('Fail', 'U6')])
# 读取csv文件
csv_file = pd.read_csv('cs.csv')
# 删掉无用的Id列、学分列
csv_file = csv_file.drop(csv_file.columns[0], axis=1, inplace=False)
csv_file = csv_file.drop(csv_file.columns[-1], axis=1, inplace=False)
# 把csv文件变成dataframe格式
df = pd.DataFrame(csv_file)
# 学号、专业、课程去重后的列表
No = list(set(df['No']))
Major = list(set(df['Major']))
Course = list(set(df['Course']))
# 建立学生-专业字典
major_dic = dict(zip(df['No'].tolist(), df['Major'].tolist()))

lists = []
listm = []
listc = []


def Proportion(lista, x):
    s1 = x.where(x >= 90).count() / x.count()
    lista.append('%.2f%%' % (s1 * 100))
    s2 = x.where((x < 90) & (x >= 80)).count() / x.count()
    lista.append('%.2f%%' % (s2 * 100))
    s3 = x.where((x < 80) & (x >= 70)).count() / x.count()
    lista.append('%.2f%%' % (s3 * 100))
    s4 = x.where(x >= 60).count() / x.count()
    lista.append('%.2f%%' % (s4 * 100))
    s5 = x.where(x < 60).count() / x.count()
    lista.append('%.2f%%' % (s5 * 100))


for i in No:
    lista = []
    lista.append(i)
    x = df[df['No'] == i]['Score']
    lista.append(np.average(list(x)))
    lista.append(df[df['No'] == i]['Course'].drop_duplicates().count())
    Proportion(lista, x)
    lists.append(tuple(lista))
lists = sorted(lists, key=lambda y: y[1])  # 按学生平均成绩排序，升序
student_list = np.array(lists, dtype=student_dtype)
student_list = pd.DataFrame(student_list)
print(student_list)

for i in Major:
    lista = []
    lista.append(i)
    x = df[df['Major'] == i]['Score']
    lista.append(df[df['Major'] == i]['No'].drop_duplicates().count())  # 人数要去重
    Proportion(lista, student_list[student_list['No'].apply(lambda a : major_dic[a]) == i]['Avg']) # 使用学生统计数据
    listm.append(tuple(lista))

Major_list = np.array(listm, dtype=Major_dtype)
Major_list = pd.DataFrame(Major_list)
print(Major_list)

for i in Course:
    lista = []
    lista.append(i)
    x = df[df['Course'] == i]['Score']
    lista.append(np.average(list(x)))
    lista.append(df[df['Course'] == i]['No'].drop_duplicates().count())
    Proportion(lista, x)
    listc.append(tuple(lista))

course_list = np.array(listc, dtype=Course_dtype)
course_list = pd.DataFrame(course_list)
print(course_list)


