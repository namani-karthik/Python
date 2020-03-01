
# A python program to create user-defined exception 
  
# class MyError is derived from super class Exception 
class MyError(Exception): 
  
    # Constructor or Initializer 
    def __init__(self, value): 
        self.value = value 
  
    # __str__ is to print() the value 
    def __str__(self): 
        return(repr(self.value)) 
  
try: 
    raise(MyError(3*2)) 
  
# Value of Exception is stored in error 
except MyError as error: 
    print('A New Exception occured: ',error.value) 
'''class myException(Exception):
    def __init__(self,arg):
        self.msg=arg
    def check(dict):
        for k,v in dict.items():
            print('Name={:15s} Balance={:10.2f}'.format(k,v))
            if(v<2000.00):
                raise myException('Balance amount is less in the account of')
    bank={'Raj':5000.00, 'Vani':8900.00, 'Ajay':1990.00, 'Naresh':3000.00}
    try:
        check(bank)
    except myException as me:
        print('hi')'''
'''
x=5
try:
    assert x!=5,'your input is five...'
    print('The number entered is',x)
except AssertionError as obj:
    print(obj)'''

'''import logging
logging.basicConfig(filename='E:\\Python\\Naresh_ex\\NT1.txt',level=logging.NOTSET)
a=4
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    logging.critical(' critical')
    logging.error(' error')
    logging.warning('Warning')
    logging.info('Info')
    logging.debug('Debug')
except Exception as e:
    print(e)'''
