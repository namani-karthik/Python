'''global z
z='G'
x = "global"
y="test"
def foo():
    global x
    y = "local"
    x = x * 2
    z='g_foo'
    print(z)
    print(x)
    print(y)
print(z)
print(x)
print(y)
foo()
print(x)
print(y)
print(z)'''


def sum(a,b):
    return (a+b)
d=sum(2,3)*10
print(d)

