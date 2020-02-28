import tkinter
from tkinter import *
x=tkinter.Tk()
sb=Scrollbar(x,orient=HORIZONTAL)
sb.pack(side=BOTTOM,fill=X)
sb1=Scrollbar(x)
sb1.pack(side=RIGHT,fill=Y)
text=Text(x,wrap=NONE,xscrollcommand=sb.set,yscrollcommand=sb1.set)
text.pack()
sb.config(command=text.xview)
sb1.config(command=text.yview)
quote="""I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again. I have a simple rule to go with all my awesome
dolphin sightings in the water: never surf a wave when you know they're cruising the lineup. They're the coolest creatures
ever, I love them to pieces and find them completely fascinating and beautiful in every way possible. But geez they're wave hogs.
The odds of this happening are slim to none when you find yourself partywaving with a dolphin, but ask this kid if he
wants to do it again.I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again.I have a simple rule to go with all my awesome
dolphin sightings in the water: never surf a wave when you know they're cruising the lineup. They're the coolest creatures
ever, I love them to pieces and find them completely fascinating and beautiful in every way possible. But geez they're wave hogs.
The odds of this happening are slim to none when you find yourself partywaving with a dolphin, but ask this kid if he
wants to do it again.I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again.I have a simple rule to go with all my awesome
dolphin sightings in the water: never surf a wave when you know they're cruising the lineup. They're the coolest creatures
ever, I love them to pieces and find them completely fascinating and beautiful in every way possible. But geez they're wave hogs.
The odds of this happening are slim to none when you find yourself partywaving with a dolphin, but ask this kid if he wants to do it again.
I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again. I have a simple rule to go with all my awesome
dolphin sightings in the water: never surf a wave when you know they're cruising the lineup. They're the coolest creatures
ever, I love them to pieces and find them completely fascinating and beautiful in every way possible. But geez they're wave hogs.
The odds of this happening are slim to none when you find yourself partywaving with a dolphin, but ask this kid if he
wants to do it again.I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again.I have a simple rule to go with all my awesome
dolphin sightings in the water: never surf a wave when you know they're cruising the lineup. They're the coolest creatures
ever, I love them to pieces and find them completely fascinating and beautiful in every way possible. But geez they're wave hogs.
The odds of this happening are slim to none when you find yourself partywaving with a dolphin, but ask this kid if he
wants to do it again.I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again.I have a simple rule to go with all my awesome
dolphin sightings in the water: never surf a wave when you know they're cruising the lineup. They're the coolest creatures
ever, I love them to pieces and find them completely fascinating and beautiful in every way possible. But geez they're wave hogs.
The odds of this happening are slim to none when you find yourself partywaving with a dolphin, but ask this kid if he wants to do it again."""
text.insert(END,quote)
x.mainloop()
