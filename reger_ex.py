import re
'''str='This is normal\nstring'
str1=r'This is normal\nstring'
print(str)
print(str1)'''

'''prog=re.compile(r'm\w\w')
str='cat mat bat rat map'
result=prog.search(str)
print('1.',result)
print('2.',result.group())
print('3.',re.findall(r'm\w\w',str))'''

'''str='Welcome to Python. It is a programming language'
result=re.split(r'\W+',str) //result is not as expected
print(result)
res=re.sub(r'to', 'too',str)
print(res)'''

'''
1. Matching strings
2. Searching for strings
3. Finding all strings
4. Splitting a string into pieces
5. Replacing strings
'''

'''str='an apple a day keeps the doctor away'
result=re.findall(r'a[\w]*',str)
for w in result:
    print(w)
    '''
'''str='an apple a day keeps the doctor away'
result=re.findall(r'\ba[\w]*\b',str)
for w in result:
    print(w)'''

'''str='The cricket match will be conducted on 1st and 2nd of every month'
result=re.findall(r'\d[\w]*',str)
for w in result:
    print(w)'''

'''str='one two three four five six seven 8 9 10'
result=re.findall(r'\b\w{5}\b',str)
print(result)'''

'''str='Karthik:9000212118'
result=re.search(r'\d+',str)
print(result.group())'''

'''str='Karthik:9000212118'
result=re.search(r'\D+',str)
print(result.group())'''

'''str='Vijay 20 1-5-2101, Rohit 33 22-10-1990, sita 22 15-09-2000'
res=re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(res)'''

'''str='Hello World'
res=re.search(r'^He',str)
if res:
    print('Starting with He')
else:
    print('Not starting with He')'''

'''str='Hello World'
res=re.search(r'World$',str)
if res:
    print('String ends with World')
else:
    print('String doesnot ends with World')'''

f=open('E:\\Python\\test.txt.txt','r')
for line in f:
    res=re.findall(r'w\w+',line)
if len(res)>0:
    print(res)
f.close()



























