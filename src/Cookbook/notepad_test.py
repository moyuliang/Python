from Tkinter import *
from self_notepad import notebook

root=Tk()
nb=notebook(root,LEFT)

f1=Frame(nb())
b1=Button(f1,text="Button 1")
e1=Entry(f1)

b1.pack(fill=BOTH,expand=1)
e1.pack(fill=BOTH,expand=1)
f2=Frame(nb())
b2=Button(f2,text="Button 2")
b3=Button(f2,text="Beep 2",command=Tk.bell)
b2.pack(fill=BOTH,expand=1)
b3.pack(fill=BOTH,expand=1)
f3=Frame(nb())

nb.add_screen(f1,"Screen 1")
nb.add_screen(f1,"Screen 2")
nb.add_screen(f3,"dummy")
root.mainloop()