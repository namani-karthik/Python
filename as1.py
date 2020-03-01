import functools as r

a=5
b=0
try:
    f=open_A_file()
    z=lambda x,y:x+y
    print(list(r.reduce(z,[1,23.3])))
    c=a/b
    if(c is int):
        pass
    if(c is float):
        pass
except TypeError:
    print('I am in TypeError exception')
except ZeroDivisionError:
    print('I am in ZeroDivisionError exception')
except:
    print('I am in General exception')
else:
    print('There are no exceptions')
finally:
    print('I am in last block')
print('Progam execution is completed')
print('Bye')
