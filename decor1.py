def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner

def num():
    return 10

v=(decor(num))
print(v())
