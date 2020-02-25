import tkinter
from tkinter import*
def hello():
	select="You selected: "
	if(var.get()==1):
		select=select+"\nMale"
	if(var1.get()==1):
		select=select+"\nFemale"
	label3.config(text=select)
x=tkinter.Tk()
x.geometry("300x300")
var=IntVar()
var1=IntVar()
label=Label(x,text="Your Sex: ")
label.pack()
label1=Label(x,text="please select...")
label1.pack()
c1=Checkbutton(x,text="Male",variable=var)
c1.pack()
c2=Checkbutton(x,text="Female",variable=var1)
c2.pack()
b=Button(x,text="Quit",command=x.quit)
b.pack()
b1=Button(x,text="Show",command=hello)
b1.pack()
label3=Label(x)
label3.pack()
x.mainloop()
