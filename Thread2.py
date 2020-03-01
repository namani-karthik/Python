from threading import *
class MyThread(Thread):
    def __init__(self,value):
        Thread.__init__(self)
        self.value=value
    def run(self):
        print('Value:',self.value)

t=MyThread(123)
t.start()

t1=MyThread(234)
t1.start()

