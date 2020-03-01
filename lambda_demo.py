'''import functools as r
a=lambda x,y:x+y
b=lambda x:x*x
c=lambda x:x%2==0

lst=[1,2,3,4,5,6,7,8,9]

print('Filter demo:',list(filter(c,lst)))
print('Reduce Demo:',(r.reduce(a,lst)))
print('Map Demo:',list(map(b,lst)))'''

lst_names_birth=[[1,1983],[2,1984],[3,1982],[4,1983],[5,1981],[6,1980],[7,1981],[8,1987],[9,1983]]

lst_lambda=['In','Python','anonymous','function','means','that','a','function','is','without','a','name']
print(lst_lambda)
Names_starting_with_a=lambda x: (x[0]=='a' or x[0]=='e' or x[0]=='i' or x[0]=='o' or x[0]=='u')
Birth=lambda x:x[1]==1985
print('Raw string:',lst_lambda)
print('Strings starting with "a" are:',list(filter(Names_starting_with_a,lst_lambda)))

print('Total employees details:',lst_names_birth)
print('Employees born in the year 1985',list(list(filter(Birth,lst_names_birth))))

                            
