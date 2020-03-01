from threading import Thread

class MyThread:
    
    def __init__(self,x,y):
        self.a=x
        self.b=y
       
    def display(self):
            print(self.a,self.b)
t=MyThread('Hello', ' Naresh Tech')
t=Thread(target=t.display)
t.start()


