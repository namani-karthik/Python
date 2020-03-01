def add(x):
    return x+10
lst=[1,2,3,4,-10]
lst1=list(map(add,lst))
lst2=list(filter(add,lst))
print('Using map function',lst1)
print('Using filter function',lst2)
