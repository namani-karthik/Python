class test():
    def __init__(self,x):
        self.value=x
        
    def __add__(self,val):
        c=self.value + val.value
        return c
    def __sub__(self,val):
        c=self.value - val.value
        return c
    
a=test(10)
b=test(20)
c=a+b # => a.add(b)
print(c)
