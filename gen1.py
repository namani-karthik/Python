def myGen(x):
    while(x>=0):
        yield(x)
        x-=1
def v():
    print('Hi')
v=myGen(5)
v()
