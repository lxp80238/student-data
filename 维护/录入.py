# 作者：林肖鹏
# 开发时间：2024/3/10 17:31


def lr():
    import 维护.建立学生类
    import time
    filename = 'D:\\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt'
    file_backup = 'D:\\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库_backup.txt'
    file = open(filename, 'r', encoding='utf=8')
    while True:
        no = input('请输入学生学号（输入“0”则返回主菜单）：')
        if no.isdigit():
            if 1000 < int(no) < 2000:
                file = open(filename, 'r+', encoding='utf=8')
                if no in file.read():
                    print('该学号已登记，请选择修改操作。')
                    pass
                else:
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
                    # file.writelines(str(维护.建立学生类.Student.dict(维护.建立学生类.Student(no, name, sc_ch, sc_ma, sc_en,
                    # sc_py)))) # 按字典格式写入文件
                    file.writelines('\n')

            elif int(no) == 0:
                break
            else:
                print('输入学号格式不正确。')
        else:
            print('输入学号格式不正确。')
    print('学生信息录入完毕！')

    # 备份信息文件
    with open(filename, 'r', encoding='utf=8') as file_y:  # with格式只允许一次读写操作后立即关闭文件
        file_backup = open(file_backup, 'a', encoding='utf=8')
        file_backup.write('\n备份日期：\n')
        file_backup.write(file_y.read())

    file.close()
    file_backup.close()
