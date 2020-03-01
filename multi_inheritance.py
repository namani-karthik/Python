class A:
    def disp(self):
        print('Inside Class A')
class B:
    def disp(self):
        print('Inside Class B')
class C(B,A):
    def disp(self):
        super().disp()
c=C()
c.disp()

