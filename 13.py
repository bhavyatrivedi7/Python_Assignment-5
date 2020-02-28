import tkinter
from tkinter import*
x=tkinter.Tk()
photo=PhotoImage(file="1.png")
text=Text(x,height=20,width=30)
text.image_create(END,image=photo)
text.pack(side=LEFT)
text1=Text(x,height=20,width=50)
sb=Scrollbar(x,command=text1.yview)
text1.config(yscrollcommand=sb.set)
text1.tag_config("big",font=("Arial",20,"bold"))
text1.tag_config("lol",font=("Arial",13,"bold"))
text1.insert(END,"\nSWAMI VIVEKA MUNDAN\n","big")
quote="""Swami Vivekananda was a Hindu monk and one of the most
 celebrated spiritual leaders of India. He was more than just a spiritual mind; 
 he was a prolific thinker, great orator and passionate patriot.
 He carried on the free-thinking philosophy of his guru, Ramakrishna Paramhansa forward
 into a new paradigm. He worked tirelessly towards betterment of the society, 
 in servitude of the poor and needy, dedicating his all for his country. 
 He was responsible for the revival of Hindu spiritualism and established 
 Hinduism as a revered religion on world stage. His message of universal brotherhood 
 and self-awakening remains relevant especially in the current backdrop of widespread political 
 turmoil around the world. The young monk and his teachings have been an inspiration to 
 many, and his words have become goals of self-improvement especially for the youth of the country. 
 For this very reason, his birthday, January 12, is celebrated as the National Youth Day in India."""
text1.insert(END,quote,"lol")
text1.pack(side=LEFT)
sb.pack(side=RIGHT,fill=Y)
x.mainloop()
