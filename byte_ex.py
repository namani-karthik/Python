'''elements=[23,7,0,13,65]
elements1=[12,56,0,0,256]
elements=bytes(elements)
#elements1=bytes(elements1)
for i in elements:print(i)
print(elements1)'''


elements=[23,7,0,13,65]
print('Original Bytearray')
for i in elements:print(i)
elements=bytearray(elements)
elements[0]=100
elements[3]=200
print('Modified Bytearray')
for i in elements:print(i)

