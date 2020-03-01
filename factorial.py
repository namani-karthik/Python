def Fact(n):
    if n==1:
        result = 1
    else:
        result = (n*Fact(n-1))
    return result
print("Please enter the number to find Factorial")
num=int(input())
print("Factorial of the Entered number (%i) is %i" %(num,Fact(num)))
