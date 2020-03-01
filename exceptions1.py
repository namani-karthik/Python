try:
    a=5
    b=0

    print(a+b)
    print(a-b)
    print(a*b)
    try:
        print(float('Hi'))
    except ValueError:
        print('There is a Type Conversion error in your code')
    print(a/b)
except ValueError:
    print('There is a Type Conversion error in your code')
except ZeroDivisionError:
    print('You cannot divide any number with zero')
except Exception:
    print('Inside the exception')
else:
    print('I am in else part')
finally:
    print('I am in Finally part')
    
