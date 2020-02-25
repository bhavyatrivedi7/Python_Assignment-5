import tkinter
from tkinter import *
from tkinter import messagebox
def hello():
	messagebox.showinfo("hello world","hello bhavya")
x=tkinter.Tk()
x.geometry("300x300")
b=tkinter.Button(x,text="ok",command=hello,height=5,width=5)
b.pack()
x.mainloop()
