import tkinter
from tkinter import*
def hello():
	select=e1.get()
	label.config(text=select)
x=tkinter.Tk()
x.geometry("300x300")
e1=Entry(x)
e1.pack()
b=Button(x,text="Copy",fg="blue",bg="yellow",font="bold",command=hello)
b.pack()
label=Label(x,text="******")
label.pack()
x.mainloop()
