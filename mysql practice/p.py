import pymysql
import mysql.connector

connection = pymysql.connect(
        host='localhost',
        user='root',
        password='MySql46.@',
        db='attendance_app'
    )
my_cursor = connection.cursor()
query = "Select * from attendance"
my_cursor.execute(query)
results = my_cursor.fetchall()
for row in results:
    print(row)
my_cursor.close()
connection.close()
