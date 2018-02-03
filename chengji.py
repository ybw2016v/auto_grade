#!python
import xlwt
import xlrd
import csv
from xlutils.copy import copy
def pretty_str(sb):
    if '　' in sb:
        newsb=''
        # print('!')
        for i in range(0,len(sb)):
            if sb[i]=='　':
                pass
            else:
                newsb=newsb+sb[i]
        return newsb
    else:
        # print("?")
        return sb
    pass
def create_dict(number):
    dicti={}
    filename=str(number)+'.csv'
    with open(filename,'r') as csvfile:
        rows = csv.reader(csvfile)
        for ping in rows:
            dicti[pretty_str(ping[0])]=(ping[7])
    print('dict create succeed')
    return dicti
    pass
class xsesb(object):
    """docstring for xsesb"""
    name='ssb.xls'
    number=0
    def __init__(self,dicti,number):
        self.dicti=dicti
        self.number=number
    def openread(self):
        rb = xlrd.open_workbook(self.name)
        self.rb=rb
        table = rb.sheets()[1]
        self.table=table
        print('there are %d rows'%table.nrows)
        pass
    def loopp(self):
        able=self.table
        for i in range(1,able.nrows):
            stuname=able.cell_value(i,0)
            if stuname in self.dicti:
                print(stuname+'OK')
            else:
                print(stuname+'F')
            pass
        wb=copy(self.rb)
        self.wb=wb
        ws=wb.get_sheet(1)
        self.ws=ws
        for i in range(1,able.nrows):
            stuname=able.cell_value(i,0)
            if stuname in self.dicti:
                ws.write(i,8,str(self.dicti[stuname]))
        wb.save(self.name)
    pass
def pretty_grade(dd):
    key=11.1#缩放系数
    if '姓名' in dd:
        del dd['姓名']
    dd1={}
    for a,b in dd.items():
        n1=dd[a]
        dd1[a]=int(key*(float(n1)**0.5)+1)
    print('pretty_grade OK')
    return dd1
    pass
for i in range(8,9):
    pass
    dd=create_dict(i)
    # for a in dd:
    #     print (a+':'+dd[a])
    a=xsesb(pretty_grade(dd),i)
    a.openread()
    a.loopp()
    print("%d班　ＯＫ"%i)