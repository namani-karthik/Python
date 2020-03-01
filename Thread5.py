from threading import *
from time import *

class movie:
    def __init__(self,str):
        self.str=str
    def movieshow(self):
        for i in range(1,6):
            print(self.str," : ",i)
            sleep(0.1)

obj1=movie('Cut ticket')
obj2=movie('Show Chair')

t1=Thread(target=obj1.movieshow)
t2=Thread(target=obj2.movieshow)

t1.start()
t2.start()
