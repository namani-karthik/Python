lst=[1,2,3,4,5]
try:
    print(lst[6])
except IndexError:
    print('Index error')
except Exception:
    print('Inside the Exception')
print('I can still write the code here')
    
