# 作   者：林肖鹏
# 开发时间：2024/3/28 9:53

def px_tol():
    import 维护.建立学生类
    import 查询.显示所有学生信息
    filename = 'D:\\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt'
    pfilename = 'D:\林肖鹏\\temp\\学生信息系统练习\\查询\\数据库（按总成绩排序）.txt'

    with open(filename, 'r', encoding='utf-8') as rfile:
        count = sum(1 for line in rfile)
        print('系统中学生总人数为{0}人。'.format(count))
        rfile.seek(0)
        students = rfile.readlines()
        students_list = [] # 方法2使用
        # pfile=open(pfilename,'w',encoding='utf-8')
        # pfile.close()
        for item in students: # 方法2使用
            c = item[0:-1]
            c_list = c.split(',')
            # c_list.append(str(int(c_list[2])+int(c_list[3])+int(c_list[4])+int(c_list[5])))
            students_list.append(c_list)
            # print(students_list)
    while True:
        t=input('1=升序；2=降序；0=返回上一级菜单：')
        if t=='1':
            ''' # 方法1
            for d in range(0,401):
                for item in students:
                    value=item[0:-1]
                    value = value.split(',')
                    if int(value[2]) + int(value[3]) + int(value[4]) + int(value[5])== d:
                        print(维护.建立学生类.Student(value[0], value[1], value[2], value[3], value[4], value[5]),
                              '总成绩：',(int(value[2]) + int(value[3]) + int(value[4]) + int(value[5])))
                        # with open(pfilename, 'a', encoding='utf-8') as pfile:
                            # pfile.writelines(item)
                    else:
                        pass
            break
            '''
            # 方法2
            with open(pfilename, 'w+', encoding='utf-8') as pfile:
                students_list.sort(key=lambda x:[int(x[2])+int(x[3])+int(x[4])+int(x[5])],reverse=False) # sort排序函数
                for value in students_list:
                    pfile.writelines('{0},{1},{2},{3},{4},{5},\n'.format(value[0], value[1], value[2], value[3], value[4],value[5]))
                pfile.seek(0)
                students = pfile.readlines()
                查询.显示所有学生信息.print_all(students)



        elif t=='2':
            # 方法1
            with open(pfilename, 'w', encoding='utf-8'):
                for d in range(401,0,-1):
                    for item in students:
                        value=item[0:-1]
                        value = value.split(',')
                        if int(value[2]) + int(value[3]) + int(value[4]) + int(value[5])== d:
                            print(维护.建立学生类.Student(value[0], value[1], value[2], value[3], value[4], value[5]),
                                  '总成绩：',(int(value[2]) + int(value[3]) + int(value[4]) + int(value[5])))
                            with open(pfilename, 'a', encoding='utf-8') as pfile:
                                pfile.writelines(item)
                        else:
                            pass
        elif t=='0':
            break
        else:
            print('输入有误!')