import tkinter
from tkinter import *
def hello():
	n1=int(e1.get())
	n2=int(e2.get())
	n3=n1+n2
	e3.insert(END,n3)
x=tkinter.Tk()
x.geometry("700x100")
label=Label(x,text="Enter Two Numbers")
label.pack()
label1=Label(x,text="Enter First Number: ")
label1.pack(side=LEFT)
e1=Entry(x)
e1.pack(side=LEFT)
label2=Label(x,text="Enter Second Number: ")
label2.pack(side=LEFT)
e2=Entry(x)
e2.pack(side=LEFT)
label3=Label(x,text="Addition: ")
label3.pack(side=LEFT)
e3=Entry(x)
e3.pack(side=LEFT)
b=Button(x,text="ADD",command=hello)
b.pack(side=LEFT)
x.mainloop()
