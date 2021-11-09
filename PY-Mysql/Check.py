import Amysql as sql
import mysql.connector
from Amysql import GetData, UpdateDB
from tkinter import *

z=GetData("inventory")

id,price,name,Stock,Catagory=[],[],[],[],[]

for i in z:
    id.append(i[0])
    name.append(i[1]) 
    price.append(i[2]) 
    Stock.append(i[3]) 
    Catagory.append(i[4]) 
option=name.copy()

a="b"
x="a"
dec={a:2,x:3}
print(dec)
#print(id);print(name);print(price);print(Stock);print(Catagory)
