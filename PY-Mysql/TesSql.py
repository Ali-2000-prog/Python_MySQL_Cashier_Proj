import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="testdb"
)

mycursor=mydb.cursor()

#sqlFormula = "INSERT INTO students (name,age) Values (%s,%s)"
sql="UPDATE students SET age= %s Where name= 'Ace'"
n=[22]
print(sql,n) 

mycursor.execute(sql,n)

#myresult=mycursor.fetchall()
mydb.commit()

#for db in myresult:
 #   print(db)
