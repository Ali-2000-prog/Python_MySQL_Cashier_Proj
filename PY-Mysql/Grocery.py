from tkinter import *
import tkinter as tk
from Amysql import GetData, UpdateDB, BillPrice, BillPriceUP




def Groceryy():
    gro=Tk()
    #gro.geometry("350x350")
    gro.title("Grocery Section")

    data=GetData('grocery')

    id,name,price,Stock=[],[],[],[]
    dicte={}
    for i in data:
        id.append(i[0])
        name.append(i[1]) 
        price.append(i[2]) 
        Stock.append(i[3])

    options=[]
    options=name.copy()
        
    
    clicked=StringVar()
    clicked.set(options[0])

    frameget=Frame(gro)
    drop = OptionMenu(frameget,clicked, *options) 
    drop.pack(pady=8)
    
    w = Spinbox(frameget, from_ = 1, to = 10) 
    w.pack(pady=5) 
    
    #index=name.index(Productname)
    #print("its in")
    #catagory=Catagory[index]
    #id_no=id[index]

    def Add():
        item=clicked.get()
        no=w.get()
        label=Label(frameget,text=item + " x " + no)
        label.pack(pady=2.4)
        income=BillPrice('grocery')
        index=name.index(item)
        Price=price[index]
        Price=int(Price) * int(no)
        Price=Price+income
        New_Stock=Stock[index] - int(no) #to be used for updating
        UpdateDB("grocery","Stock",New_Stock,index+1)

        

        BillPriceUP(Price,'grocery')
        



    AddButton=Button(frameget, text="Add",command=Add)
    AddButton.pack(pady=2)
    
    
    frameget.pack(pady=5,padx=50)
    
    gro.mainloop()

def snacks():
    gro=Tk()
    #gro.geometry("350x350")
    gro.title("Snacks Section")

    data=GetData('snacks')

    id,name,price,Stock=[],[],[],[]
    dicte={}
    for i in data:
        id.append(i[0])
        name.append(i[1]) 
        price.append(i[2]) 
        Stock.append(i[3])

    options=[]
    options=name.copy()
        
    
    clicked=StringVar()
    clicked.set(options[0])

    frameget=Frame(gro)
    drop = OptionMenu(frameget,clicked, *options) 
    drop.pack(pady=8)
    
    w = Spinbox(frameget, from_ = 1, to = 10) 
    w.pack(pady=5) 
    
    def Add():
        item=clicked.get()
        no=w.get()
        label=Label(frameget,text=item + " x " + no)
        label.pack(pady=2.4)
        income=BillPrice('snacks')
        index=name.index(item)
        Price=price[index]
        Price=int(Price) * int(no)
        Price=Price+income
        New_Stock=Stock[index] - int(no) #to be used for updating
        UpdateDB("snacks","Stock",New_Stock,index+1)

        BillPriceUP(Price,'snacks')
        
    AddButton=Button(frameget, text="Add",command=Add)
    AddButton.pack(pady=2)
    
    frameget.pack(pady=5,padx=50)
    
    gro.mainloop()

def appliances():
    gro=Tk()
    #gro.geometry("350x350")
    gro.title("Appliances Section")

    data=GetData('appliances')

    id,name,price,Stock=[],[],[],[]
    dicte={}
    for i in data:
        id.append(i[0])
        name.append(i[1]) 
        price.append(i[2]) 
        Stock.append(i[3])

    options=[]
    options=name.copy()
        
    
    clicked=StringVar()
    clicked.set(options[0])

    frameget=Frame(gro)
    drop = OptionMenu(frameget,clicked, *options) 
    drop.pack(pady=8)
    
    w = Spinbox(frameget, from_ = 1, to = 10) 
    w.pack(pady=5) 
    
    def Add():
        item=clicked.get()
        no=w.get()
        label=Label(frameget,text=item + " x " + no)
        label.pack(pady=2.4)
        income=BillPrice('appliances')
        index=name.index(item)
        Price=price[index]
        Price=int(Price) * int(no)
        Price=Price+income
        New_Stock=Stock[index] - int(no) #to be used for updating
        UpdateDB("appliances","Stock",New_Stock,index+1)

        BillPriceUP(Price,'appliances')
        
    AddButton=Button(frameget, text="Add",command=Add)
    AddButton.pack(pady=2)
    
    frameget.pack(pady=5,padx=50)
    
    gro.mainloop()
