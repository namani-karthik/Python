from tkinter import *
def buttonClick(self):
    print('This is working')

def buttonClick1(self):
    print('This is also working')
def buttonClick_right(self):
    root1=Tk()
    f1=Frame(root,height=1000,width=1000,bg="red", cursor='cross')
    f1.pack()
    
    
root=Tk()
f=Frame(root,height=1000,width=1000,bg="blue", cursor='cross')
f.propagate(0)

b=Button(f,text='Karthik', width=5,height=2,bg='yellow',fg='blue',
         activebackground='green',activeforeground='red')
f.pack()
b.pack()
b.bind('<Button-1>',buttonClick)
b1=Button(f,text='Karthik', width=15,height=2,bg='yellow',fg='blue',
         activebackground='green',activeforeground='red')
f.pack()
b1.pack()
b1.bind('<Button-1>',buttonClick1)
b1.bind('<Button-3>',buttonClick_right)
       
root.mainloop()



'''#Program to dispaly the Root dimensions
from tkinter import *
from tkinter import font
root=Tk()
root.title('Karthik')
#root.geometry("1400*300")
c=Canvas(root,bg="red", height=700, width=1200, cursor='pencil')
#id=c.create_oval(50,50,400,300,width=4,fill="white")
id=c.create_arc(500,100,800,300,width=3,start=90,extent=180,outline="yellow", style="arc")
id=c.create_image(500,200,anchor=NE,image=file1,activeimage=file2)
c.pack()
#Program to display the Root Window
from tkinter import *
root=Tk()
root.mainloop()'''
