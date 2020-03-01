from tkinter import *

r=Tk()
def callback():
    print('this is working')
r.title("Karthik")
r.geometry("200x150+300+300")
b=Button(r,text="ok",command=callback)
b.pack()
r.mainloop()
