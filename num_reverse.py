a=int(input('Pls enter a number'))
sum=0
while(a>0):
    sum=sum*10+(a%10)
    a=a//10
print(sum)
    
