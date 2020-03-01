import functools

def add(x,y):
    return(x*y)

lst=[1,2,3,4,5]
result=functools.reduce(lambda x,y:x+y,lst)
print(result)

#lst=[['A','12-08-1985'],['B','12-02-1985'],['C','12-08-1985'],['D','12-01-1985']]
#Even_numbers=list(filter(lambda x:x[1][3:5]=='08',lst))
#print(Even_numbers)

'''def add(x):
    if(x%2==0):
        return 'Even'
    else:
        return 'False'

lst=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x=='Even' ,map(add,lst)))
print(result)'''

