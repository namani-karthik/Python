class Animal:
    def __init__(self,a,b):
        self.Name=a
        self.color=b
    def display(self):
        print(self.Name,self.color)

'''class dog():
    def display(self):
        print('I am inside the dog class')'''

class puppy(Animal):
    def __init__(self,a,b,c):
        self.type=c
        super().__init__(a,b)
        
    def display(self):
        super().display()
        print(self.type)

p=puppy('Puppy','Brown',3)
p.display()
