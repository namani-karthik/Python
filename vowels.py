s=['Andhra Pradesh','Telangana','Keral']
str=''
v_list=[]
for i in s:
    for j in i:
        if(j in {'a','e','i','o','u','A','I','U','O','E'}):
            str=str+j
    v_list.append(str)
    str=''
print(v_list)
