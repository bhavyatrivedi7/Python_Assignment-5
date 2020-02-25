import tkinter
from tkinter import*
def hello():
	select=var.get()
	selection=""
	if(select==1):
		selection=selection+"You are not Eligible"
	if(select==2):
		selection=selection+"You are Eligible"
	label1.config(text=selection)
x=tkinter.Tk()
x.geometry("300x300")
label=Label(x,text="Your Age: ")
label.pack()
var=IntVar()
r1=Radiobutton(x,text="Less Than 18",value=1,variable=var,command=hello)
r1.pack()
r2=Radiobutton(x,text="More Than 18",value=2,variable=var,command=hello)
r2.pack()
label1=Label(x)
label1.pack()
x.mainloop()
