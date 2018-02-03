#!python
import csv
import random
print('hi')
filename='评语.csv'
filename2='教师评语导入模板.csv'
filename3='教师评语导入模板2.csv'
datedog=[]
datedog2=[]
datedog3=[]
number=0
with open(filename,'r') as csvfile:
    rows = csv.reader(csvfile)
    for ping in rows:
        datedog.append(ping)
        pass
        print('倒入评语：')
    for i in datedog:
        print(i[0])
        pass
    number=len(datedog)
    print('共倒入%d条评语'%(len(datedog)))
with open(filename2,'r') as dog1:
    xdog=csv.reader(dog1)
    for ping in xdog:
        datedog2.append(ping)
    number2=len(datedog2)
    print('导入前：')
    for i in range(1,number2):
        print(datedog2[i][2])
        pass
for i in range(1,len(datedog2)):
    datedog2[i][2]=datedog[random.randint(0,number-1)][0]
    hug=datedog2[i][1]
    lutdog='\''+hug
    datedog2[i][1]=lutdog
    pass
    for lo in datedog2:
        print(lo)
with open(filename3,'w',newline='') as dog2:
    pudog=csv.writer(dog2)
    pudog.writerows(datedog2)



