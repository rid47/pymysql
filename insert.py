import pymysql

db = pymysql.connect("localhost","","","test")

cursor = db.cursor()

sql = "INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)\
VALUES ('%s','%s','%d','%c','%d')"%\
('Ridwan','Mizan',20,'M',2000)
try:
	cursor.execute(sql)
	db.commit()
except pymysql.InternalError as error:
    code, message = error.args
    print(">>>>>>>>>>>>>", code, message)
    db.rollback()

db.close()
