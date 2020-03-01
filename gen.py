def mul_10(x,y):
    while(x<=y):
        if(x%10==0):
            yield x
        x=x+1
f=mul_10(10,100)
for i in f:
    print(i)



