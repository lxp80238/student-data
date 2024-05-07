# 作者：
# 开发时间：2024/3/10 18:46
# github

import 维护.录入
import 查询.按学号查询
import 查询.按学号排序
import 查询.按总成绩排序
import 维护.按学号删除
import 维护.按学号修改
import 查询.显示所有学生信息

print('------------------------欢迎使用学生信息系统（学号1001至1999）-------------------------')
file = open( 'D:\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt', 'r', encoding='utf=8')
count = sum(1 for line in file)
print('系统中学生总人数为{0}人。'.format(count))

while True: # 无限循环
    r=input('请输入操作代码\033[4;31;44m（1=录入；2=修改；3=查询，4=删除；5=排序；6=统计；7=显示所有学生信息；0=退出）：\033[0m')
    if r in ['1','2','3','4','5','6','7','0']:
        if r == '1':
            维护.录入.lr()
        elif r == '2':
            维护.按学号修改.xg_no()
        elif r == '3':
            查询.按学号查询.cx_no()
        elif r == '4':
            维护.按学号删除.sc_no()
        elif r == '5':
            while True:
                s = input('请输入操作代码（1=按学号；2=按姓名；3=按语文，4=按数学；5=按英语；6=按Python；7=按总成绩；0=返回上一级菜单）：')
                if s == '0':
                    break
                elif s == '1':
                    查询.按学号排序.px()
                elif s == '2':
                    pass
                elif s == '3':
                    pass
                elif s == '4':
                    pass
                elif s == '5':
                    pass
                elif s == '6':
                    pass
                elif s == '7':
                    查询.按总成绩排序.px_tol()
                else:
                    print('输入不正确。')
        elif r=='6':
            filename = 'D:\林肖鹏\\temp\\学生信息系统练习\\维护\\数据库.txt'
            file = open(filename, 'r', encoding='utf=8')
            count=len(file.readlines())
            # count = sum(1 for line in file)
            file.close()
            print('系统中学生总人数为{0}人。'.format(count))
        elif r == '7':
            查询.显示所有学生信息.show()
        else:
            print('系统已退出,谢谢使用！')
            break
    else:
        print('输入有误!')

file.close()

# 更新测试
# 2024.5.7

