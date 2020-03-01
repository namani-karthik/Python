from threading import *
def display(str,str1):
    print(str+str1)
t=Thread(target=display,args=('hello','hi',))
t.start()
