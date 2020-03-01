import functools
lis = [ 1 , 3, 5, 6, 2,1]
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a*b,lis))
