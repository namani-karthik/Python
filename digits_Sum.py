a=1234
while(a//10>0):
    sum=0
    while(a//10>0):
        sum=sum+a%10
        a//=10
    a=sum+a
print(sum)
