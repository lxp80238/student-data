# 作者：林肖鹏
# 开发时间：2024/3/10 17:00

# 修改学生信息

def xg_no():
    filename_t = 'D:\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库_temp.txt'
    file_backup = 'D:\\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库_backup.txt'
    import linecache
    import os
    import 维护.建立学生类
    from 维护.建立学生类 import Student

    filename='D:\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt'
    file = open(filename, 'r', encoding='utf=8')
    while True:
        no = input('请输入需修改的学生学号（输入“0”返回主菜单）：')
        if no.isdigit():
            if no == '0':
                break
            else:
                if 1000 < int(no) < 2000:
                    file = open(filename, 'r', encoding='utf=8')
                    count = sum(1 for line in file)
                    tol = []
                    for f in range(1, count + 1):
                        a = linecache.getline(filename, f)
                        linecache.clearcache()
                        a = a[0:-1]
                        value = a.split(',')
                        tol.append(value[0])
                        # print(tol)
                    if no in tol:
                        for e in range(1, count + 1):
                            d = linecache.getline(filename, e)
                            linecache.clearcache()
                            if no not in d:
                                file_temp = open(filename_t, 'a', encoding='utf=8')
                                file_temp.writelines(d)
                            else:
                                continue
                        file_temp = open(filename_t, 'r', encoding='utf=8')
                        file = open(filename, 'w', encoding='utf=8')
                        file.write(file_temp.read())
                        file_temp.close()
                        os.remove(filename_t)
# 删除后添加信息
                        file = open(filename, 'a', encoding='utf=8')
                        name = input('姓名：')
                        while True:
                            sc_ch = (input('语文成绩：'))
                            if sc_ch.isdecimal():
                                break
                            else:
                                print('输入格式不正确。')
                        while True:
                            sc_ma = (input('数学成绩：'))
                            if sc_ma.isdecimal():
                                break
                            else:
                                print('输入格式不正确。')
                        while True:
                            sc_en = (input('英语成绩：'))
                            if sc_en.isdecimal():
                                break
                            else:
                                print('输入格式不正确。')
                        while True:
                            sc_py = (input('Python成绩：'))
                            if sc_py.isdecimal():
                                break
                            else:
                                print('输入格式不正确。')

                        print(维护.建立学生类.Student(no, name, sc_ch, sc_ma, sc_en, sc_py))
                        file.writelines([no, ',', name, ',', sc_ch, ',', sc_ma, ',', sc_en, ',', sc_py])
                        # file.writelines(str(维护.建立学生类.Student.dict(维护.建立学生类.Student(no, name, sc_ch, sc_ma, sc_en, sc_py)))) # 按字典格式写入文件
                        file.writelines('\n')

                    else:
# 无学生信息直接添加新信息
                        while True:
                            t = input('系统无此学号信息！是否录入学生信息（1=是；0=返回主菜单）？')
                            if t == '0':
                                break
                            elif t == '1':
                                file = open(filename, 'a', encoding='utf=8')
                                name = input('姓名：')
                                while True:
                                    sc_ch = (input('语文成绩：'))
                                    if sc_ch.isdecimal():
                                        break
                                    else:
                                        print('输入格式不正确。')
                                while True:
                                    sc_ma = (input('数学成绩：'))
                                    if sc_ma.isdecimal():
                                        break
                                    else:
                                        print('输入格式不正确。')
                                while True:
                                    sc_en = (input('英语成绩：'))
                                    if sc_en.isdecimal():
                                        break
                                    else:
                                        print('输入格式不正确。')
                                while True:
                                    sc_py = (input('Python成绩：'))
                                    if sc_py.isdecimal():
                                        break
                                    else:
                                        print('输入格式不正确。')

                                print(维护.建立学生类.Student(no, name, sc_ch, sc_ma, sc_en, sc_py))
                                file.writelines([no, ',', name, ',', sc_ch, ',', sc_ma, ',', sc_en, ',', sc_py])
                                # file.writelines(str(维护.建立学生类.Student.dict(维护.建立学生类.Student(no, name, sc_ch, sc_ma, sc_en, sc_py)))) # 按字典格式写入文件
                                file.writelines('\n')

                                break
                            else:
                                print('输入有误，请重新输入!')
                else:
                    print('输入学号范围应为：1001至1999，请重新输入')
        else:
            print('输入格式不正确。')

    file.close()

    # 备份信息文件
    with open(filename, 'r', encoding='utf=8') as file_y:  # with格式只允许一次读写操作后立即关闭文件
        file_backup = open(file_backup, 'a', encoding='utf=8')
        file_backup.write('\n备份日期：\n')
        file_backup.write(file_y.read())
        file_backup.close()

    file.close()



