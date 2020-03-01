from threading import *

class vihaan():
    def __init__(self,str):
        self.str=str
    def disp(self,x,y):
        print(self.str)
        print('The args are:',x,y)
obj=vihaan('Hello Vihaan')
t1=Thread(target=obj.disp,args=(1,2))
t1.start()

'''def disp(str):
    print('Hello',str)

for i in range(5):
    t=Thread(target=disp,args=('vihaan',))
    t.start()'''
