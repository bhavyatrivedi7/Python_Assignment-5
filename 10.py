import tkinter
from tkinter import*
def hello(val):
	sender=val.widget
	num=sender.curselection()
	value=sender.get(num)
	var.set(value)
x=tkinter.Tk()
x.geometry("300x300")
x.title("BoxList")
listbox=Listbox(x)
listbox.insert(1,"PHP")
listbox.insert(2,"ROR")
listbox.insert(3,"PYTHON")
listbox.insert(4,"ANDROID")
listbox.insert(5,"IOS")
listbox.bind("<<ListboxSelect>>",hello)
listbox.pack()
var=StringVar()
label=Label(x,textvariable=var)
label.pack()
x.mainloop()
