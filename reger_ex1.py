import re
'''
f=open('regex.txt','r')

for line in f:
    res=re.findall(r'\S+@\S+',line)
if(len(res)>0):
   print(res)
f.close()

'''

f1=open(r'regex1.txt','r')
f2=open(r'reg.txt','w')

for line in f1:
    res1=re.search(r'\d{4}',line)
    print(res1.group())
    f2.write(res1.group()+"\t")
f1.close()
f2.close()
