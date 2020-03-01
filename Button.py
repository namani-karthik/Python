from tkinter import *

#defining Class
class MyButton:
    def __init__(self, root):
        #create frame as child to the root
        self.f=Frame(root,height=200,width=300)

        #Let the frame will not shrink
        self.f.propagate(0)

        #Attach the frame to root Window
        self.f.pack()

        #Create a Push buttonas child to the frame and bind it to buttonClick Method
        self.b = Button(self.f, text='My', highlightcolor='green',width=15, height=3, bg='yellow', fg='blue',
                        activebackground='green', activeforeground='red',command=self.buttonClick)


        self.b.pack()
    def buttonClick(self):
        print('Its working')

root=Tk()
root.wm_title('Karthik')
root.clipboard_clear()
root.resizable(width=True, height=True)
m=MyButton(root)

root.mainloop()
        
