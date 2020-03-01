class dog():
    count=0
    def __init__(self):        
        dog.count+=1
    @classmethod
    def noObjects(cls):
        print('Number of Total dog_objects created are:',dog.count)
    @staticmethod
    def noObjects1():
        print('Number of Total dog_objects dispalyed using static are:',dog.count)


p=dog()
j=dog()
t=dog()
a=dog()
dog.noObjects()
p.noObjects1()
