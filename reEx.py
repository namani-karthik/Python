from threading import *
from time import *

class Theatre():
    def __init__(self,str):
        self.str=str
    def mainshow(self):
        for i in range(1,6):
            print(self.str+':',i)
            sleep(0.1)
obj1=Theatre('Cut ticket')
obj2=Theatre('Show Movie')
t1=Thread(target=obj1.mainshow)
t2=Thread(target=obj2.mainshow)
t1.start()
t2.start()
   
