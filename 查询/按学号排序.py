# 作   者：林肖鹏
# 开发时间：2024/3/13 10:28

def px():
    import linecache
    import 维护.建立学生类
    import 查询.显示所有学生信息

    filename= 'D:\\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt'
    pfilename='D:\\林肖鹏\\temp\\学生信息系统练习\\查询\\数据库（按学号排序）.txt'
    file = open(filename, 'r', encoding='utf=8')
    count = sum(1 for line in file)
    print('系统中学生总人数为{0}人。'.format(count))
    file.close()
    with open (pfilename,'w+',encoding='utf-8') as pfilename:
        for d in range(1001, 2000):
            for e in range(1, count + 1):
                a = linecache.getline(filename, e)
                linecache.clearcache()
                # print(a)
                a = a[0:-1]
                # print(a)
                value = a.split(',')
                if int(value[0]) == d:
                    ap_str = '{0},{1},{2},{3},{4},{5},\n'.format(value[0], value[1], value[2], value[3], value[4],
                                                                 value[5])
                    pfilename.writelines(ap_str)
                else:
                    pass
            else:
                pass
        else:
            pass
        pfilename.seek(0)
        students = pfilename.readlines()
        查询.显示所有学生信息.print_all(students)
