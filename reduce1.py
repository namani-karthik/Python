import functools as r
def func(x,y):
    print(x,y)
l=lambda x,y:func(x,y)
lst=[1,2,3,4,5]
print(r.reduce(l,lst))
