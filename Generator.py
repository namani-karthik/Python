def myGen(x,y):
    while(x<=y):
        yield(x)
        x+=1

v=myGen(0,10)

print(next(v))
print(next(v))
print(next(v))
print(next(v))
