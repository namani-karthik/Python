file_read=open('data.txt','r')
file_write=open('data1.txt','w')
str=file_read.readlines()
x=[]
y=[]
for i in str:
    a,b=i.split()
    x.append(a)
    y.append(b)
file_write.write('x values:')
for i in x:
    file_write.write(i+' ')
file_write.write('\n')
file_write.write('y values:')
for i in y:
    file_write.write(i+' ')


file_write.close()  
file_read.close()
