import tkinter
from tkinter import*
def hello():
	select="you selected: "
	if(var.get()==1):
		select=select+"\nBananas"
	if(var1.get()==1):
		select=select+"\nChicken"
	if(var2.get()==1):
		select=select+"\nStuffed Peppers"
	label1.config(text=select)
x=tkinter.Tk()
x.geometry("300x300")
var=IntVar()
var1=IntVar()
var2=IntVar()
label=Label(x,text="Choose your favourite food: ")
label.pack()
c1=Checkbutton(x,text="Bananas",variable=var)
c1.pack()
c2=Checkbutton(x,text="Chicken",variable=var1)
c2.pack()
c3=Checkbutton(x,text="Stuffed Peppers",variable=var2)
c3.pack()
b=Button(x,text="ok",command=hello)
b.pack()
label1=Label(x)
label1.pack()
x.mainloop()
