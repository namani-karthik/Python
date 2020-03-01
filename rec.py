import functools 
def Is_Even(x):
    if(x%2==0):
        return True
    else:
        return False
lst=[0,1,2,3,4,5,6,7,8,9]
lst1=list(reduce(lambda x,y:x+y,lst))
print(lst1)

'''y=lambda x,y:x*y
z=lambda x,y:x-y
print(y([1,2,3,4],40))
print(z(5,40))
def rec(x):
    if(x==1):
        return 1;
    else:
        return x*rec(x-1)
print(rec(5))'''

        
