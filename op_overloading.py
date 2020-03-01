class book:
    def __init__(self,a):
        self.pages=a
    def __add__(self,other):
        return self.pages+other.pages

X_book=book('abc')
Y_book=book('zxy')
print(X_book+Y_book)
