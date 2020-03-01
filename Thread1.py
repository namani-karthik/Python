from threading import *

def display(name,name1):
    print('I am in display function called by ',name, name1)

for i in range(5):
    t=Thread(target=display, args=('Naresh','Python'))
    t.start()
