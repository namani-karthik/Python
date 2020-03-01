x=int(input('Enter a number: '))

def prime(a):
    flag=False
    for i in range(2,a):
        if(a%i==0):
            flag=True
            break   
    return flag


if(prime(x)):
        print('Entered number is not prime')
else:
        print('Prime')
        
