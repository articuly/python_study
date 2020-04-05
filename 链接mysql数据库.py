import mysql.connector

# 链接数据库
cnx = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='mycms')

# 创建游标对象cursor
cursor = cnx.cursor()

# 创建数据表
sql = 'create table book(`book_id` int not null, `book_name` char(32) not null , `book_author` char(32) not null , `book_pubdate` datetime not null, primary key (`book_id`));'

try:
    cursor.execute(sql)
except Exception as e:
    print(sql)
    print(e)
else:
    print('table has been created.')

cursor.close()
cnx.close()
