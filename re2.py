import re
str='Hello World'
res=re.search(r'^He',str)
if(res):
    print('string starts with "He"')
else:
    print('Str doesnt start with "He"')


res=re.search(r'World$',str)
if(res):
    print('string ends with "World"')
else:
    print('Str doesnt end with "World"')
