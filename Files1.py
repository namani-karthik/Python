import os
f=open('e:\\nareshfile.txt','r')
if os.path.isfile('e:\\nareshfile.txt'):
    f=open('e:\\nareshfile.txt','r')
else:
    print('file doesnt exists')

l=w=c=0
for line in f:
    words=line.split()
    l+=1
    w+=len(words)
    c +=len(line)
print(l)
print(w)
print(c)
f.close()

