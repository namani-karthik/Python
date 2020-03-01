from tkinter import *
root=Tk()
c=Canvas(root,bg='white',height=700,width=1200)

file=PhotoImage(file='E:\\MyBinaryfile.gif')

id=c.create_image(500,200,anchor=SW,image=file)

c.pack()
root.mainloop()
