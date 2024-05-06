# 作   者：林肖鹏
# 开发时间：2024/3/28 9:33

def show():
    filename = 'D:\\林肖鹏\\temp\\学生信息系统练习\\查询\\数据库（按学号排序）.txt'
    with open(filename, 'r', encoding='utf-8') as rfile:  # with语句打开文件，省去close操作。
        students = []
        students = rfile.readlines()
        print_all(students)

def print_all(students):
    format = '{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(format.format('序号','学号', '姓名', '语文成绩', '数学成绩', '英语成绩', 'Python成绩', '总成绩'))
    nu = 1
    for item in students:
        item = item[0:-1]
        value = item.split(',')
        print('\033[0;36;41m',format.format(nu,value[0], value[1], value[2], value[3], value[4], value[5],
                            (int(value[2]) + int(value[3]) + int(value[4]) + int(value[5]))),'\033[0m')
        nu=nu+1