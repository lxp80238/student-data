# 作者：林肖鹏
# 开发时间：2024/3/10 17:05

class Student():
    def __init__(self,no,name,sc_ch,sc_ma,sc_en,sc_py):
        self.no=no
        self.name=name
        self.sc_ch=sc_ch
        self.sc_ma=sc_ma
        self.sc_en=sc_en
        self.sc_py=sc_py
    def __str__(self):
        return '学号：{0}，姓名：{1}，语文：{2}，数学：{3}，英语：{4}，Python：{5}'.format(self.no,self.name,self.sc_ch,self.sc_ma,self.sc_en,self.sc_py)

    def list(self):
        return [self.no,self.name,self.sc_ch,self.sc_ma,self.sc_en,self.sc_py]

    def dict(self):
        return {'学号': self.no, '姓名': self.name, '语文': self.sc_ch, '数学': self.sc_ma,'英语': self.sc_en, 'py': self.sc_py}

if __name__ == '__main__':
    st1=Student(5,5,5,5,6,5)
    print(st1)
    print(st1.dict())
    print(st1.list())
