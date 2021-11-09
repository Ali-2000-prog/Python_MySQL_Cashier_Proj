from tkinter import *
import tkinter as tk
from Amysql import GetData, IntoTable, UpdateDB

def UpdateInventory():
    # It should update the price or the items in inventory
    UpdateItem=Tk()
    UpdateItem.geometry("220x290")
    UpdateItem.title("Add Item")
    label=Label(UpdateItem, text="Super Store", font=("Arial Bold", 16))
    label.pack()
    labelx=Label(UpdateItem, text="     ").pack()# used for spacig
    frameAIU=Frame(UpdateItem)

    # Item Name
    namelabel = Label(frameAIU, text="Item Name: ").grid(row=0,column=0)
    nentry = Entry(frameAIU); nentry.grid(row=1,column=0)
    labelx=Label(frameAIU, text="     ").grid(row=2,column=0)# used for spacig
    
    Ulabel = Label(frameAIU, text="Enter: ").grid(row=3,column=0)
    Uentry = Entry(frameAIU); Uentry.grid(row=4,column=0)
    labely = Label(frameAIU, text="     ").grid(row=5,column=0)# used for spacig

    def UPN():
        Productname = nentry.get().title()
        # to check if name exists
        z=GetData("inventory")
        id=[]; name=[];price=[]; Stock=[]; Catagory=[]

        for i in z:
            id.append(i[0])
            name.append(i[1]) 
            price.append(i[2]) 
            Stock.append(i[3]) 
            Catagory.append(i[4]) 

        if Productname in name:
            index=name.index(Productname)
            print("its in")
            catagory=Catagory[index]
            id_no=id[index]
            
            if type(Uentry.get())==str:
                Uenty=Uentry.get().title()
                print("string")
            else:
                Uenty=Uentry.get()
                print("not string")

            UpdateDB("inventory","name",Uenty,id_no)

            id_sub=[]; name_sub=[]
            x=GetData(catagory)
            for i in x:
                id_sub.append(i[0])
                name_sub.append(i[1])

            index_sub=name_sub.index(Productname)

            id_no_sub=id_sub[index_sub]
            print(id_no_sub)
        
            if catagory == "Grocery":
                UpdateDB("grocery","name",Uenty,id_no_sub)
            elif catagory == "snacks":
                UpdateDB("snacks","name",Uenty,id_no_sub)
            elif catagory == "appliances":
                UpdateDB("appliances","name" ,Uenty,id_no_sub)
                    
        else:
            print("not in")# to give a messagebox
        
    def UPP():
        Productname = nentry.get().title()
        # to check if name exists
        z=GetData("inventory")
        id=[]; name=[];price=[]; Stock=[]; Catagory=[]

        for i in z:
            id.append(i[0])
            name.append(i[1]) 
            price.append(i[2]) 
            Stock.append(i[3]) 
            Catagory.append(i[4]) 

        if Productname in name:
            index=name.index(Productname)
            print("its in")
            catagory=Catagory[index]
            id_no=id[index]
            print(id_no)
            UpdateDB("inventory","price",Uentry.get(),id_no)

            id_sub=[]; name_sub=[]
            x=GetData(catagory)
            for i in x:
                id_sub.append(i[0])
                name_sub.append(i[1])

            index_sub=name_sub.index(Productname)

            id_no_sub=id_sub[index_sub]
            
            if catagory == "grocery":
                UpdateDB("grocery","price",Uentry.get(),id_no_sub)
            elif catagory == "snacks":
                UpdateDB("snacks","price",Uentry.get(),id_no_sub)
            elif catagory == "appliances":
                UpdateDB("appliances","price" ,Uentry.get(),id_no_sub)
                
        else:
            print("not in")# to give a messagebox
        

    NameUpdate=Button(frameAIU,text="Update Product name",command=UPN).grid(row=6,column=0)
    labelz=Label(frameAIU, text="     ").grid(row=7,column=0)# used for spacig

    B1=Button(frameAIU,text="Update Price", command=UPP).grid(row=8,column=0)

    frameAIU.pack()

    UpdateItem.mainloop()

#UpdateInventory()

def CheckInventory():
    # Inventory should give the details
    pass

def AddItem():
    # Acess the database and in the table created add the item that can be retrieved 

    AddItem=Tk()
    AddItem.geometry("220x290")
    AddItem.title("Add Item")
    label=Label(AddItem, text="Super Store", font=("Arial Bold", 16))
    label.pack()
    frameAI=Frame(AddItem)

    # Item Name
    namelabel = Label(frameAI, text="Item Name: ").grid(row=0,column=0)
    nentry = Entry(frameAI);nentry.grid(row=1,column=0)
    
    #Item price
    Plabel = Label(frameAI, text="Price: ").grid(row=2,column=0)
    Pentry = Entry(frameAI); Pentry.grid(row=3,column=0)

    #Item Stock
    Slabel = Label(frameAI, text="New Stock: ").grid(row=4,column=0)
    Sentry = Entry(frameAI); Sentry.grid(row=5,column=0)

    #Item Catagory
    Clabel = Label(frameAI, text="Catagory: ").grid(row=6,column=0)
    Centry = Entry(frameAI); Centry.grid(row=7,column=0)

    #Item Stock_price
    SPlabel = Label(frameAI, text="Buying Stock Price: ").grid(row=8,column=0)
    SPentry = Entry(frameAI); SPentry.grid(row=9,column=0)

    labelx=Label(frameAI, text="     ").grid(row=10,column=0)# used for spacig

    def EnterItem(): #a command function for entry ADDITem
        name= nentry.get(); price= Pentry.get(); stock= Sentry.get(); catagory= Centry.get(); stock_price= SPentry.get() 
        catagory=catagory.title()
        name=name.title();  
        val=[(name,price,stock,catagory,stock_price)]
        IntoTable("inventory",val)
    
    # Enter into Database Button
    DbButton=Button(frameAI, text = "Enter Item",command=EnterItem).grid(row=11,column=0)
    
    frameAI.pack()
    AddItem.mainloop()