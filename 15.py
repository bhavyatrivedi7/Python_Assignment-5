import tkinter
from tkinter import*
x=tkinter.Tk()
x.geometry("300x300")
label=Label(x,text="This is Times Now",font="Times",fg="red")
label.pack()
label1=Label(x,text="This is Helvetica",font="Helvetica",fg="white",bg="green")
label1.pack(fill=X)
label2=Label(x,text="This is Verdana Bold",font=("Verdana",13,"bold"),fg="blue",bg="yellow")
label2.pack()
x.mainloop()
