def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner

def decor1(fun):
    def decor():
        value=fun()
        return value*2
    return decor

@decor
@decor1
def num():
    return 10

print(num())

