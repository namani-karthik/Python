import functools as r
lst=['1','2','3','4','5']
red=lambda x,y:x+' '+y
print('Result of the reduce function:',r.reduce(red,lst))


'''squares=lambda x:x*x
lst=[0,1,2,3,4,5,6,7,8,9]
lst1=list(map(squares,lst))
print('Original list:',lst)
print('Squares of the Given list is:',lst1)'''


'''birth=lambda x:x[1]==1984
lst_id_birth=[[1,1983],[2,1984],[3,1982],[4,1984],[5,1981],[6,1980],[7,1981],[8,1987],[9,1983]]
print('Original String List:',lst_id_birth)

print('********')

print('Resultant output:',list(filter(birth,lst_id_birth)))'''

'''
lambda_func=lambda x:x[0]=='a'
lst_lambda=['In','Python','anonymous','function','means','that','a','function','is','without','a','name']
print('Original String List:',lst_lambda)
lst=list(filter(lambda_func,lst_lambda))
print('Resultant list:',lst)

'''

'''def IsEven(lst):
    lst1=[]
    for x in lst:
        if(x%2==0):
           lst1.append(x)
    return lst1


lst=[1,2,3,4,5,6,7,8,9]
#print('Even numbers in the List:',IsEven(lst))

even=lambda x:x%2
for x in lst:
    print(even(x))
print('****'
print('Demo on Filters:',list(filter(even,lst)))
'''

#lst_names_birth=[[1,1983],[2,1984],[3,1982],[4,1983],[5,1981],[6,1980],[7,1981],[8,1987],[9,1983]]


