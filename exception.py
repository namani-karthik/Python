try:
    lst=[1,2]
    print(lst[0])
    try:
        a=int('Hi')
    except:
        print('Inner Exception')
    b=0
    c=a/b
    print(c)
except IndexError:
    print('Exception due to wrong indexing')
except ZeroDivisionError :
    print('Exception due to zero division')
except Exception as e:
    print('Exception occured',e)
else:
    print('No exception occured')
finally:
    print('Inside finally')
print('Program execution completed')
