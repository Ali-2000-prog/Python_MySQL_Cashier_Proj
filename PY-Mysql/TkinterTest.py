from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk


win = tk.Tk()

v = tk.StringVar()
def setText(word):
    v.set(word)

a = ttk.Button(win, text="plant", command=setText("plant"))
a.pack()
b = ttk.Button(win, text="animal", command=setText("animal"))
b.pack()
c = ttk.Entry(win, textvariable=v)
c.pack()
win.mainloop()

'''
photo = PhotoImage(file="im.png")
label_ = Label(root,image=photo)
label_.place(x=20,y=-16)
        
root.mainloop()'''

'''
v= tk.IntVar()

#radioB1 = Radiobutton(root, Variable=0, value=0, text = "Radio Button 1" , command=lambda:print(v.get()))
items=["a",'b','c','d','e','f','g','h']
ii=0
for i in items:
    radioButton = Radiobutton(root, variable=v, value=ii, text=i)
    radioButton.pack()
    ii+=1
#radioButton2 = Radiobutton(root, variable=v, value=1, text="Radio 2")

B=Button(root, text="check",command=lambda:print(v.get(),a))

#radioButton1.pack()
#radioButton2.pack()
B.pack()
root.mainloop()
'''
'''
mb=Menubutton(root, text="this is menu")
mb.menu=Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1", command=lambda:print("Option 2"))
mb.menu.add_command(label="Option 2", command=lambda:print("Option 2"))
mb.pack()
root.mainloop()'''

'''
c=Canvas(root, height=250, width = 300 ,bg='blue')
l=c.create_line(5,20,200,200, width=10,fill="red")

c.pack()

root.mainloop()
'''

'''
L=Label(root,text="Hello World")
L.pack(side=LEFT)

def BFunction():
    L1=Label(root, text="Click ME clicked")
    L1.pack()

B1=Button(root, text="Click me!", command=BFunction)
B1.pack(side=RIGHT)

B2=Button(root, text="Click me!", command=BFunction)
B2.pack(side=BOTTOM)
root.mainloop()'''

'''
def see():
    def testt():
        print(w.get())

    master = Tk() 
    w = Spinbox(master, from_ = 0, to = 10) 
    w.pack(pady=5) 
    B=Button(master,text="check",command=testt)
    B.pack(pady=5)
    master.mainloop() 


def DD():

    def fun():
        print("test")
        
        abel=Label(root,text=clicked.get())
        abel.pack()
        abel.config(text="any")

    root=Tk()
    options=[
        "ace","brace","chace"
    ]
    clicked=StringVar()
    clicked.set(options[0])

    drop = OptionMenu(root,clicked, *options) 
    drop.pack(pady=10)

    B=Button(root,text="check",command=fun)
    B.pack(pady=5)

    root.mainloop()

DD()
'''