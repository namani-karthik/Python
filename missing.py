import logging
logging.basicConfig(filename='E:\\Python\\Naresh_ex\\NT1.txt',level=logging.ERROR)
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
    print(e)






'''class myException(Exception):
    def __init__(self,arg):
        self.msg=arg
        
    def check(dict):
        for k,v in dict.items():
            print('Name={:15s} Balance={:10.2f}'.format(k,v))
            if(v<2000.00):
                raise myException('Balance amount is less in the account of',k)
            
    bank={'Raj':5000.00, 'Vani':8900.00, 'Ajay':1990.00, 'Naresh':3000.00}
    
    try:
        check(bank)
    except myException as me:
        print(me)
'''





'''class MyError(Exception): 
  
    # Constructor or Initializer 
    def __init__(self, value): 
        self.value = value 
  
    # __str__ is to print() the value 
    def __str__(self): 
        return((self.value)) 
  
try: 
    raise(MyError(3*2)) 
  
# Value of Exception is stored in error 
except MyError as error: 
    print('A New Exception occured: ',error.value)

'''





'''a='hi'
b=12
lst=[1,2,3]
try:
    print(lst[6])
except Exception as obj:
    print('Following exception occured in ur code:',obj)'''

'''x=5
try:
    assert x==5,'your input is not five...'
    print('No Exception....The number entered is',x)
except Exception as obj:
    print(obj)
except AssertionError as obj:
    print(obj)'''



    
'''def add(a=None,b=None,c=None):
    if(a!=None and b!=None and c!=None):
        print('The sum is:',a+b+c)
    elif(a!=None and b!=None):
        print('The sum is:',a+b)
    elif(a!=None):
        print('The sum is:',a)
    else:
        print('Please pass the values')

add(1,2,3)
add(1,2)
add(1)
add()'''
