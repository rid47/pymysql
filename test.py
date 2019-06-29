import pymysql

db = pymysql.connect("localhost","","","test")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS employee")

sql = '''CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME
 CHAR(20), AGE INT, SEX CHAR(1), INCOME FLOAT) '''

cursor.execute(sql)
# data = cursor.fetchone()

# print("Database version: %s"% data)

db.close()