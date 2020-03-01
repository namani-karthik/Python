def display(fargs,**kwargs):
    print('First argument is:', fargs)
    for x,y in kwargs.items():
        print(x,y)


display(3,rno='2222',marks=333)
print('*****************************')
display('Naresh',rno='1111',marks=120,Name='SUltan')
print('*****************************')
display('Technologies',rno='3333',marks=100,Name='raja',Address='Hyderabad')
