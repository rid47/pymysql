import pymysql

db = pymysql.connect("localhost","","","test")

cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'"%(1000)
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		print("fname = %s,lname = %s, age = %d,sex = %s, income = %d"%\
			(fname,lname,age,sex,income))
	#print(results)
	#db.commit()
except:
	print("Error: unable to fetch data")


db.close()