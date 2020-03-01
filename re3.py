import re
str='one two three four five six seven dhree'
result=re.findall(r't[\w]*\Z',str)
print(result)
