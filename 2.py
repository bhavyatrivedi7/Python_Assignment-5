import tkinter
from tkinter import*
def hello():
	select="You selected option: "+(var.get())
	label.config(text=select)
x=tkinter.Tk()
x.geometry("200x200")
var=StringVar()
r1=Radiobutton(x,text="python",variable=var,value=1,command=hello)
r1.pack()
r2=Radiobutton(x,text="perl",variable=var,value=2,command=hello)
r2.pack()
r3=Radiobutton(x,text="java",variable=var,value=3,command=hello)
r3.pack()
r4=Radiobutton(x,text="C++",variable=var,value=4,command=hello)
r4.pack()
r5=Radiobutton(x,text="C",variable=var,value=5,command=hello)
r5.pack()
label=Label(x)
label.pack()
x.mainloop()