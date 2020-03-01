def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner
def decor1(fun):
    def inner():
        value=fun()
        return value*2
    return inner

#@decor1
#@decor
def num():
    return 10

f=(decor1(decor(num())))
print(f)
