a=5
b=3
lst=[1,2]
try:
    print(a/b)
    print(lst[3])
    print('hi')
except TypeError:
    print('There is type error in the code')
except ZeroDivisionError:
    print('Divisor should not be zero')
except Exception:
    print('There is an Exception in the code')
else:
    print('Inside the else block')
finally:
    print('Inside the finally block')
