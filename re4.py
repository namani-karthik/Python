import re
f=open('Naresh.txt')
str=f.read()
res=re.search(r'\w+@\w+.com',str)


print(res.group())
