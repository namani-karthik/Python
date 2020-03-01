#WAP to 

'''#WAP to sum all the multiple of 3,4,5,7,9 btwn 0-100

def sum_num():
    sum=0
    for i in range(0,11,1):
        if((i%3==0)or(i%4==0)or(i%5==0)or(i%7==0)or(i%9==0)):
            sum=sum+i
    print('Sum of the given assignment is ',sum)

sum_num()'''





'''#WAP to reverse a string using while loop
str2='Hi, Welcome to python World'
def str_rev(str1):
    x=len(str1)
    while(x>=0):
        print(str1[x-1])
        x=x-1;
print(str_rev(str2))'''
