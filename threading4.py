from threading import *
from time import *

class Tea:
    def PrepareTea(self):
        sleep(5)
        self.Task1()
        self.Task2()
        self.Task3()
    def Task1(self):
        print('Boil Milk and tea power for 5 minutes....',end=' ')
        sleep(5)
        print('Done')
    def Task2(self):
        print('Add sugar and boil for 3 minutes....',end='')
        sleep(3)
        print('Done')
    def Task3(self):
        print('Filter and serve it....',end=' ')
        print('Done')
t=Tea()
obj=Thread(target=t.PrepareTea)
obj.start()
