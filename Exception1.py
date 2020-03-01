'''
try:
    a=2
    b=0
    c=list(a)
    print(a/b)
except ZeroDivisionError:
    print('Inside ZeroDivisionError exception')
except TypeError:
    print('Inside Type Error')
except:
    print('Inside the General Exception')
else:
    print('Inside else Statement')
finally:
    print('Inside the Finally Statement')
'''

a=2
b=3.4+7j
c=a+b
print(c)
