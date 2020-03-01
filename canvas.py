from tkinter import *
root=Tk()

c=Canvas(root,bg='blue',height=700,width=1200,cursor='cross')

id=c.create_line(50,50,200,50,200,150,width=14,fill='Red')

id=c.create_oval(100,100,400,300,width=5,fill='yellow',outline='red'
                 ,activefill='green')

id=c.create_polygon(10,10,200,200,300,200,width=3,fill='green',outline='red',
                    smooth=1,activefill='lightblue')

id=c.create_rectangle(500,200,700,600,width=2,fill='gray',outline='black',activefill='yellow')

fnt=('Times',40,'bold italic')
id=c.create_text(500,100,text='My Canvas',font=fnt,fill='yellow',activefill='green')


c.pack()
root.mainloop()
