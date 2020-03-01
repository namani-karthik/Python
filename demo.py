def Add(fargs,*args):
    sum1=0
    for x in args:
        sum1=sum1+x
    print('The sum of the given values is:',fargs+sum1)


Add(1)
Add(1,2)
Add(1,2,3)
Add(1,2,3,4,5,6,7,8,9,10)

