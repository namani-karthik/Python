'''
m,n=[int(i) for i in input('Please enter two numbers m and n separated by ",":').split(',')]
x=m
if x%2!=0:
    x=x+1
while x>=m and x<=n:
    print(x)
    x+=2
'''
'''
Flag=False
n=int(input('Enter upper limit: '))
for x in range(2,n+1):
    for y in range(2,x):
          if(x%y)==0:
              break
          if(x-1==y):
              print(x)
              
'''
'''
lst=[1,2,3,4,5,6,7,8,9]
sum=0;
for x in lst:
    sum=sum+x
print('Total sum of all values in the List is',sum)
'''


'''
lst=['Sum',1,2,3,True]
sum=0;
for x in lst:
    if type(x) is int:
        sum=sum+x        
print('Total sum of all values in the List is',sum)
'''


'''
x1 = int(input('Please enter number to search: '))
Flag=False
lst=[1,2,3,4,5,6,7,8,9]
for x in lst:
    if x==x1:
        Flag=True
        break
if(Flag):
    print('Element found')
else:
    print('Element not found')
'''



for x in range(1,11):
    print('*'*x,end='')
    print()




n=10
for x in range(1,11):
    print(' '*n,end='')
    print('* '*(x))
    n-=1

