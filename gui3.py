from tkinter import *

def buttonClick1(self):
    print('Left Click')

root=Tk()
f=Frame(root,height=200,width=300)


f.propagate(0)

f.pack()

b=Button(f, text='My Button', width=15, height=2, bg='blue', fg='yellow', activebackground='green')

b.pack()
b.bind("<Button-3>",buttonClick)
root.mainloop()
