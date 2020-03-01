'''def Gen(n):
    for x in n:
        yield (x*x)
lst=[1,2,3,4,5]
new_numbers=Gen([1,2,3,4,5])
new=list(new_numbers)
print(new_numbers)
print(new)
for x in new_numbers:
    print(x)'''

def fact(n):
    if(n==0):
        return 1
    else:
        return (n*fact(n-1))
print('Factorial of 5 is:',fact(5))
