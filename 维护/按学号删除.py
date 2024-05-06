# 作者：林肖鹏
# 开发时间：2024/3/10 17:01

def sc_no():
    import linecache
    import os
    filename = 'D:\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt'
    filename_t = 'D:\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库_temp.txt'
    file_backup = 'D:\\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库_backup.txt'
    file = open(filename, 'r', encoding='utf=8')
    count = sum(1 for line in file)
    print('系统中学生总人数为{0}人。'.format(count))
    tol = []

    while True:
        no = input('请输入需删除的学生学号（输入“0”返回主菜单）：')
        if no.isdigit():
            if no == '0':
                break
            else:
                if 1000 < int(no) < 2000:
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
                        file = open(filename, 'r', encoding='utf=8')
                        count = sum(1 for line in file)
                        print('学号为{0}的学生信息删除完毕，系统中学生总人数变更为{1}人。'.format(no,count))
                        file = open(filename, 'r', encoding='utf=8')

                    else:
                        print('系统无此学号信息！')
                else:
                    print('输入学号格式不正确。')
        else:
            print('输入学号格式不正确。')

    # 备份信息文件
    with open(filename, 'r', encoding='utf=8') as file_y:  # with格式只允许一次读写操作后立即关闭文件
        file_backup = open(file_backup, 'a', encoding='utf=8')
        file_backup.write('\n备份日期：\n')
        file_backup.write(file_y.read())

    file.close()
