from functools import *
def add (x,y):
    return x*y
lst=[1,2,3,4,5]
print(reduce(add,lst))
