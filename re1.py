import re

f=open('E:\\Python\\Naresh_ex\\NT1.txt','r')
for line in f:
    res=re.findall(r'\b[\S]*@[\S]*',line)

if(len(res)>0):
    print(res)

f.close()
'''str='vijay 20 01-05-2001, mohit 21 22-10-1990, sita 22 15-09-2000'
res=re.findall(r'\d{2}-\d{2}-\d{4}',str)

for word in res:
    print(word)

str='This; is the: "Core" python\'s book'
result=re.split(r'\W',str)
print(result)

prog=re.compile(r'm\w\w')
str='cat mat bat rat map'
result=prog.search(str)
print(result.group())'''

'''str='rat man sun mop run'
result=re.match(r'm\w\w',str)
if result:
    print(result.group())'''

