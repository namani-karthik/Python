from threading import *
from time import *

class Railway:

    def __init__(self,available):
        self.available=available
        self.l=Lock()

    def reserve(self,wanted):
        self.l.acquire()
        print('Available no of berth= ', self.available)

        if(self.available >= wanted):
            name=current_thread().getName()
            print('%d berths allotted for %s \n' %(wanted,name))
            sleep(1.5)
            self.available-=wanted
        else:
            print('Sorry, no berths to allot')
        self.l.release()
obj=Railway(1)
t1=Thread(target=obj.reserve, args=(1,))
t2=Thread(target=obj.reserve, args=(1,))
t1.setName('First Person')
t2.setName('Second Person')
t1.start()
t2.start()
