class A:
    def __init__(self,a):
        self.property=a
    def display(self):
        self.property=100000+self.property
    def disp():
        print('Hi')
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.property=b
    def display(self):
        super().display()
        print('Property:',self.property)  
b=B(10000,20000)
b.display()

