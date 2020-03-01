import numpy as np 
a = np.array([1.0,5.55, 123, 0.567, 25.532]) 

print ('Original array:') 
print (a )

print ('After rounding:' )
print (np.around(a) )
print (np.around(a, decimals = 1))
