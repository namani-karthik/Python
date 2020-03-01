def Add(fargs,*kargs):
    sum=0
    for i in kargs:
        sum=sum+i
    print('Sum of the given number is',sum+fargs)
Add(1)
Add(1,2)
Add(1,2,3)
Add(1,2,3,4)
Add(1,2,3,4,5)
Add(1,2,3,4,5,6)

'''def price(item=10,value=10):
    print(item,value)


price(55)
price(555,5555)


def func(a,b):
    print(a,b)

func(10,10)
func(10,'hi')'''


'''def Arth(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f

c,d,e,f=Arth(10,20)
print(c,d,e,f)


def func():
    print('I am inside a function')
def func1(str):
    print('I am inside a function',str)
func()
func1('Welcome Python class')'''
