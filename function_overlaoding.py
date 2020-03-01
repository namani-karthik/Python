def add(a=None,b=None):
    if(a!=None and b!=None):
        return a+b
    elif(a!=None):
        return a
    else:
        return b
print(add(1))
print(add(1,2))
