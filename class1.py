class P:
    a=5
    b=6
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def disp(self):
        print('The values of the variables are P class',self.a,self.b)
class W:
    def disp1(self):
        print('Inside the W class')
class Q(P,W):
    s=5
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.s=z
    def disp2(self):
        print('Inside the child class Q',self.s)
  
q=Q(3,4,5)
q.disp1()
q.disp()

