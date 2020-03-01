from tkinter import *
root=Tk()
root.title('Frame')
def buttonClick(self):
    print('You clicked me')
f=Frame(root,height=400,width=500,bg='yellow',cursor='cross')
f.propagate(0)
f.pack()
b=Button(f,text='Click_me',width=15,height=2,bg='red',fg='blue',activebackground='green',activeforeground='red')
b.pack()
b.bind("<Button-1>",buttonClick)
root.mainloop()

'''c=Canvas(root,bg='red',height=700,width=1200,cursor='pencil')
id=c.create_line(50,50,200,50,200,150,width=4,fill='blue')
c.pack()'''
