import pymysql

db = pymysql.connect("localhost","","","test")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE>'%d'" %(20)
try:
	cursor.execute(sql)
	db.commit()
except:
	print("Error")
	db.rollback()

db.close()