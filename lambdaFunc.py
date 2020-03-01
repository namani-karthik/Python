#Is_Even=lambda x: x%2==0

def karthik(x):
    if(x%2==0):
        return 'even'
    else:
        return 0
lst1=[1,2,3,4,5,6,7,8,9]
lst=list(filter(lambda x:x%2==0,lst1))
print(lst)
