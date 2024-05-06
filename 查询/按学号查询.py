# 作者：林肖鹏
# 开发时间：2024/3/10 18:59

def cx_no():
    import linecache
    from 维护.建立学生类 import Student

    filename='D:\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt'
    while True:
        no = input('请输入需查询的学生学号（输入“0”返回主菜单）：')
        if no.isdigit():
            if no == '0':
                break
            else:
                if 1000 < int(no) < 2000:
                    file = open(filename, 'r', encoding='utf=8')
                    count = sum(1 for line in file)
                    file.close()
                    print('系统中学生总人数为{0}人。'.format(count))
                    tol = []
                    for f in range(1, count + 1):
                        a = linecache.getline(filename, f)
                        linecache.clearcache()
                        a = a[0:-1]
                        value = a.split(',')
                        tol.append(value[0])
                        # print(tol)

                    # 只查到第一个同学号（或同名）信息，程序还需修改
                    '''
                    if no in tol:
                        e = tol.index(no)  
                        a = linecache.getline(filename, e + 1)
                        linecache.clearcache()
                        value = a.split(',')
                        st = Student(value[0], value[1], value[2], value[3], value[4], value[5])
                        print(st)
                    else:
                        print('系统无此学号信息！')
                    '''

                    # 查到所有同学号（或同名）信息
                    if no in tol:
                        with open (filename,'r',encoding='utf-8') as rfile: # with语句打开文件，省去close操作。
                            format='{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
                            print(format.format('学号','姓名','语文成绩','数学成绩','英语成绩','Python成绩','总成绩'))
                            students=rfile.readlines()
                            for item in students:
                                item = item[0:-1]
                                value = item.split(',')
                                if no in value:
                                    print(format.format(value[0], value[1], value[2], value[3], value[4], value[5],(int(value[2]) + int(value[3]) + int(value[4]) + int(value[5]))))
                                else:
                                    pass
                    else:
                        print('系统无此学号信息！')
                else:
                    print('输入学号范围应为：1001至1999，请重新输入')
        else:
            print('输入格式不正确。')




