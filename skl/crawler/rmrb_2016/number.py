#测试用
#使用sqlite，存储每天的文章数，方便number取值，及给文件命名
import sqlite3
import os
import re

conn = sqlite3.connect('./number.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE rmrb
       (
       date           TEXT    NOT NULL,
       number            INT     NOT NULL);''')

path = "/人民日报/test/"
dirs = os.listdir(path)
#########
# cursor.execute("insert into rmrb (date,number) values ('2020.11.11',5)")
########
for file in dirs :
    date = re.findall('\d\d\d\d.\d\d.\d\d',file)[0] #【人民日报 2016.01.04 第7版布成良】
    print("date   ", date)
    sql = "select * from rmrb where date=?"
    cursor.execute(sql, (date,))
    values = cursor.fetchall()
    print("values   ", values)
    if values == []:
        number = 1
        sql = "insert into rmrb(date,number) values (? ,?)"
        cursor.execute(sql, (date, number))
    else:
        number = values[0][1] + 1
        sql = "update rmrb set number = ? where date = ?"
        cursor.execute(sql, (number, date))
conn.commit()

sql = "select * from rmrb "
print("****************************************************")
cursor = cursor.execute(sql,)
for row in cursor:
    print(row[0], row[1])
cursor.close()
conn.close()