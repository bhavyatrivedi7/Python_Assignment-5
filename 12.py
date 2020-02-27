import tkinter
from tkinter import*
x=tkinter.Tk()
sb=Scrollbar(x)
sb.pack(side=RIGHT,fill=Y)
listbox=Listbox(x,yscrollcommand=sb.set)
for i in range(100,151):
	listbox.insert(END,i)
listbox.pack()
sb.config(command=listbox.yview)
x.mainloop()
