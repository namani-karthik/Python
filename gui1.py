from tkinter import *

root=Tk()

c=Canvas(root,bg='white',height=700,width=1200,cursor='cross')

id=c.create_arc(100,100,400,300,width=3,start=270,extent=180,outline='red',style='arc')

c.pack()

root.mainloop()
