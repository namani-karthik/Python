class Bookx:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
    def __sub__(self,other):
        return self.pages-other.pages
class Booky(Bookx):
    def __init__(self,pages):
        self.pages=pages

b1=Bookx(500)
b2=Booky(200)
print('Total Pages=',b2-b1)
print('Total Pages=', b2+b1)
