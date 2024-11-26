import mysql.connector
import pymysql

mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'MySql46.@',
    db='attendance_app'
    
)
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE users")

# my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     print(db)

#create tables 
# create_table_query = """
# Create table if not exists attendance(
# id int auto_increment primary key,
# name varchar(100) not null,
# timestamp datetime not null
# )
# """
#execute
#Delete table records
query = "DELETE FROM attendance"

try:
    my_cursor.execute(query)
    print("table delted")

except pymysql.MySQLError as e:
    print(f'Error: {e}')
finally:
    mydb.commit()
    my_cursor.close()
    mydb.close()



  