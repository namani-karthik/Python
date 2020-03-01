from threading import *
from time import *

class MyThread:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()
        
    def task1(self):
        print('Boil the milk and add tea power for 5 minutes...\n')
        sleep(5)
        print('Done')
    def task2(self):
        print('Add sugar and boil for another 3 minutes...\n')
        sleep(3)
        print('Done')
    def task3(self):
        print('Filter it and serve it...\n')
        print('Done')

tea=MyThread()
t=Thread(target=tea.prepareTea)
t.start()
t.join()
