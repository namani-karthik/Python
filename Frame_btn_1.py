from tkinter import *

def Myfunction(self):
    print('You clicked me')
    print('Thanks for clicking me...')
def Myfunction1(self):
    print('Please dont click my right button')

root=Tk()

f=Frame(root,height=200,width=300)

f.propagate(0)

f.pack()

b=Button(f,text='Left Click',width=15,height=2,bg='yellow',fg='blue',
         activebackground='green',activeforeground='red')
b.pack()
b.bind('<Button-1>',Myfunction)

b1=Button(f,text='Right Click',width=15,height=2,bg='yellow',fg='blue',
         activebackground='green',activeforeground='red')
b1.pack()
b1.bind('<Button-2>',Myfunction1)

root.mainloop()
