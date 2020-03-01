a=2
print(a)
def func():
    global a
    a=3
    print(a)
print(a)
func()
