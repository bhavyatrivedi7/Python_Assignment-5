import tkinter
from tkinter import*
x=tkinter.Tk()
x.geometry("300x300")
b=Button(x,text="red",bg="red")
b.pack()
b1=Button(x,text="yellow",bg="yellow")
b1.pack()
b2=Button(x,text="pink",bg="pink")
b2.pack()
b3=Button(x,text="green",bg="green")
b3.pack()
b4=Button(x,text="purple",bg="purple")
b4.pack()
b4=Button(x,text="orange",bg="orange")
b4.pack()
b4=Button(x,text="blue",bg="blue")
b4.pack()
x.mainloop()

#OR

'''import tkinter
from tkinter import*
x=tkinter.Tk()
x.geometry("300x300")
colours=["red","yellow","pink","green","purple","orange","blue"]
for c  in colours:
	b=Button(text=c,bg=c)
	b.pack()
x.mainloop()'''
