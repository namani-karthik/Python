from threading import Thread

class MyThread():
    def display(self,value,v):
        print('I am inside a method: ',value)

obj=MyThread()

t=Thread(target=obj.display,args=(123,))

t.start()
