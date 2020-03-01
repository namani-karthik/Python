t.start()
t.join([timeout])
t.is_alive()
t.setName(name)
t.getName()
t.name
t.setDaemon(flag)
t.isDaemon()

from tkinter import *

class MyButton:
    def __init__(self,root):
        self.f = Frame(root,height=200, width=300)
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f, text='My Button', width=15, height=2, bg='blue', fg='yellow',
                      activebackground='green',command=lambda: self.buttonClick(1))
        self.b2=Button(self.f, text='My Button', width=15, height=2, bg='blue', fg='yellow',
                      activebackground='green',command=lambda: self.buttonClick(2))
        self.b3=Button(self.f, text='My Button', width=15, height=2, bg='blue', fg='yellow',
                      activebackground='green',command=lambda: self.buttonClick(3))
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

    def buttonClick(self,num):
        if(num==1):
            self.f['bg']='red'
        if(num==2):
            self.f['bg']='green'
        if(num==3):
            self.f['bg']='yellow'


root=Tk()

mb=MyButton(root)

root.mainloop()
