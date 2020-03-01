def outfunc(text1):
    text=text1
    def innerfunc():
        print(text)
    return innerfunc


f=outfunc('Hello')
print(f)
