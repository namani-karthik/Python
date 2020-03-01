n=int(input('Enter a lower limit:'))
n1=int(input('Enter a upper limit:'))
print('Following are the prime numbers in the given range:')


for x in range(n,n1+1,1):
    i=2h
    flag=False
    while(i<=x-1):
        if(x%i==0):
            flag=True
            break
        i=i+1
    if(flag==False):
        print(x)
