from tkinter import *

class MyButton:
    def __init__(self,root):
        self.f=Frame(root,height=200,width=300)
        self.f.propagate(0)
        self.f.pack()

        self.b=Button(self.f,text='My Button', width=15,height=2, bg='red', activebackground='green',command=self.display)
        #self.b.bind('<Button-1>',self.display)
        self.b.pack()
    def display(self):
        print('Reporting done')

root=Tk()

mb=MyButton(root)

root.mainloop()
