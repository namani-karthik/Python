def decor(func):
    def inner():
        number=func()
        return number+2
    return inner

def decor1(func):
    number=func()
    return number+2

@decor
def num():
    return 10

print((num()))


