import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    )  

def createDatabase(db):
    print(db)
    
    mycursor=mydb.cursor()
    sql="Create Database "+db
    mycursor.execute(sql)
    print("DataBase",db, "CREATED")

def DropDatabase(db):
    print(db)
    mycursor=mydb.cursor()
    sql="Drop Database "+db
    mycursor.execute(sql)
    print("DataBase",db, "Droped")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database=""
    ) 

def CreateTable(tname,db):
    mydb.database=db
    # This function does not create a custom table it creates a table in a database that exists with no parameters special
    #It has only id ,name and age: Can be further adltered
    mycursor=mydb.cursor()
    sql="Create Table "+db+"(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INTEGER (10))"
    mycursor.execute(sql)
    print("Table",tname, "Created")

def IntoTableB(cname,valuesB=list):
    db="ace"
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database=db
    )    
 
    mycursor=mydb.cursor()
    sql="INSERT INTO "+ cname + " (name,price,Stock,Stock_price) VALUES (%s,%s,%s,%s)"

    valB=valuesB
    mycursor.executemany(sql,valB)
    mydb.commit()

#Values takes argument in list form enclosed in tuple
def IntoTable(tname,cname,values=list,valueB=list):
    #ace is here is testing database
    db="ace"
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database=db
    )    
 
    mycursor=mydb.cursor()
    sql="INSERT INTO "+ tname + " (name,price,Stock,Catagory,Stock_price) VALUES (%s,%s,%s,%s,%s)"

    val=values
    mycursor.executemany(sql,val)
    mydb.commit()
    valB=valueB
    IntoTableB(cname,valB)
    print("Table",tname, "Added Values")



def DeleteRow(id,arg):
    db="ace"
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database=db
    )
    arge=str(arg)
    mycursor=mydb.cursor()
    sql="DELETE FROM "+db+" Where "+id+"="+arge
    mycursor.execute(sql)
    mydb.commit()
    print("Row Deleted Where "+id+"="+arge)  

# write update (table_name) SET (column to update)=(update)  Where id = (id no)
def UpdateDB(tname,columnUpdate,Update,id_no):
    db="ace"
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database=db
    )
    
    id_no=str(id_no)
    mycursor=mydb.cursor()
    sql="UPDATE "+tname+" SET "+columnUpdate +" =  %s  Where id = %s"
    val=(Update,id_no)

    mycursor.execute(sql,val)
    mydb.commit()
    print("Updated")

def GetData(tname):
    db="ace"
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database=db
    )
    
    mycursor=mydb.cursor()
    sql="Select * FROM " + tname
    mycursor.execute(sql)
    print("Got Data")
    myresult=mycursor.fetchall()
    l=[]
    for data in myresult:
        l.append(data) 
        #print(data)
    return l

def BillPrice(idno):
    db="ace"
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database=db
    )
    Billdict={"grocery": 1, "snacks":2, "appliances":3, "total":4} 
    mycursor=mydb.cursor()
    z=str(Billdict[idno])
    sql="Select price from bill where id= "+ z

    val=1
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    return myresult[0][0]
    
def BillPriceUP(price,name):
    Billdict={"grocery": 1, "snacks":2, "appliances":3, "total":4}
    UpdateDB("bill","price",price,Billdict[name])
