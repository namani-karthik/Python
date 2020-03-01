class Add():
    def Sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print('The sum of the numbers is',a+b+c)
        elif(a!=None and b!=None):
            print('The sum of the numbers is',a+b)
        else:
            print('Please enter two numbers to add')
    def Sum(self,a,b):
        print('Hi')
x=Add()
x.Sum(2,3,4)
x.Sum(2,3)

