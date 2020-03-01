def decor(func):
    def inner():
        value=func()
        return value+2
    return inner

def decor1(func):
    def inner():
        value=func()
        return value*2
    return inner

@decor
def func():
    return 10

result_func=int(decor(func()))
print(result_func)
