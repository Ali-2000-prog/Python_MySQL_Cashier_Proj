from tkinter import *
import tkinter as tk
from Amysql import BillPrice, IntoTable, BillPriceUP
from MenuFunc import AddItem, UpdateInventory
from Grocery import Groceryy, appliances, snacks




root=Tk()
root.geometry("350x350")
#root.title("title")

#MenuBAR
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='Inventory', menu=filemenu) 
filemenu.add_command(label='Update Inventory', command = UpdateInventory) 
filemenu.add_command(label='Check Inventory') #adding command later
filemenu.add_command(label='Add Item', command = AddItem) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command = root.quit) 

#Main Root Window
frame=Frame()

label=Label(frame, text="Super Store", font=("Arial Bold", 16))
label.pack()
frame.place(relx=0.5,rely=0.1,anchor=CENTER)

frame2=Frame(root)
labelx=Label(frame2, text="     ")# used for spacig
labelz=Label(frame2, text="     ")# used for spacing
button = tk.Button(frame2, text='Grocery', width=15,bg="#4BA1EC", command=Groceryy) 
button.grid(row=0,column=0)
labelx.grid(row=1)
button1 = tk.Button(frame2, text='Snack', width=15,bg="#4BA1EC", command=snacks) 
button1.grid(row=2,column=0)
labelz.grid(row=3)
button2 = tk.Button(frame2, text='Appliances', width=15,bg="#4BA1EC", command=appliances) 
button2.grid(row=4,column=0)

frame2.place(relx=0.2,rely=0.25)
    
frame3=Frame(root)
bill_entr=IntVar()
bill=Entry(frame3,font=('calibre',10,'normal'))

li=[BillPrice('grocery'),BillPrice('snacks'),BillPrice('appliances'),BillPrice('total')]
x=li[0]+li[1]+li[2]+li[3]
bill.grid(row=1,columnspan=2)
bill.insert(0,x)

def newButton():
    bill.delete(0,END)
    BillPriceUP(0,'grocery')
    BillPriceUP(0,'snacks')
    BillPriceUP(0,'appliances')
    BillPriceUP(0,'total')
    lii=[BillPrice('grocery'),BillPrice('snacks'),BillPrice('appliances')]
    xx=lii[0]+lii[1]+lii[2]
    bill.insert(0,xx)

def checkButton():
    bill.delete(0,END)
    lii=[BillPrice('grocery'),BillPrice('snacks'),BillPrice('appliances')]
    xx=lii[0]+lii[1]+lii[2]
    bill.insert(0,xx)

labelz3=Label(frame3, text="     ")
labelz3.grid(row=2)
checkButton=Button(frame3, text="Check", width=15,bg="#4BA1EC", command=checkButton)
checkButton.grid(row=3)

checkButton=Button(frame3, text="New", width=15,bg="#4BA1EC", command=newButton)
checkButton.grid(row=4)

frame3.place(relx=0.5,rely=0.75,anchor=CENTER)

root.mainloop()