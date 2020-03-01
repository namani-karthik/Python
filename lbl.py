from tkinter import *

class test:
    def __init__(self,root):
        self.f = Frame(root,height=350, width=500)
        self.f.propagate(0)
        self.f.pack()

        self.b1=Button(self,text="Click me",height=2,width=15, command=self.buttonClick)
        self.b2=Button(self,text="Quit", height=2, width=15, command=quit)

        self.b1.pack()
        self.b2.pack()
        self.b1.grid(row=0,column=1)
        self.b2.grid(row=0,column=2)

        def buttonClick(self):
            self.lbl = Label(self.f,text="Welcome to Python", width=20, height =2)
            self.lbl.grid(row=2,column=0)


root=Tk()

mb=test(root)
root.mainloop()
