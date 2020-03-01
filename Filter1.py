def Is_Even(x):
    if(x%2==0):
        return True
    else:
        return False
lst=[2,4,5,7,1,8]
#print(list(filter(Is_Even,lst)))
print(list(filter(lambda x:x%2==0,lst)))
