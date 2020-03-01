ele =[20,30,10]
x = bytes(ele)
y=bytearray(ele)
y[0]=77
for i in x : print(i)
for j in y : print(j)
