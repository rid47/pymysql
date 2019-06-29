import pymysql

db = pymysql.connect("localhost","","","test")

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE='%d' WHERE SEX = '%c'"%(22,'M')
try:
	cursor.execute(sql)
	db.commit()
except:
	print("Error")
	db.rollback()

db.close()