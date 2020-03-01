def sum1(fargs,*args):
    s=0
    for x in  args:
        s=s+x
    s=s+fargs
    print('Sum of the given numbers is', s)

sum1(2,3)
sum1(3,4,5,6)
sum1(8,6,8,9,10)
sum1(1,2,3,4,5,6,7,8,9)
