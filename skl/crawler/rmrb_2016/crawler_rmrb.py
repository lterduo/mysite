import re
from crawler_content import json_save
import os
import sqlite3

#一天有多篇，定义一个number
conn = sqlite3.connect('./number.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE rmrb
       (
       date           TEXT    NOT NULL,
       number            INT     NOT NULL);''')

#将要处理的文件保存在一个目录下
path = "/人民日报/2004/"

dirs = os.listdir(path)
for file in dirs :
    print('file  ', file)
    date = re.findall('\d\d\d\d.\d\d.\d\d',file)[0] #【人民日报 2016.01.04 第7版布成良】
    print("date   ", date)

    sql = "select * from rmrb where date=?"
    cursor.execute(sql, (date,))
    values = cursor.fetchall()
    if values == []:
        number = 1 #没有记录则number为1
        sql = "insert into rmrb(date,number) values (? ,?)"
        cursor.execute(sql, (date, number))
    else:
        number = values[0][1] + 1 #有记录number+1
        sql = "update rmrb set number = ? where date = ?"
        cursor.execute(sql, (number, date))

    json_save(path, file, number)

    