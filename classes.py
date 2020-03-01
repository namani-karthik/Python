class dog:
    name='Donkey'
    color='white'
    breed='A'
    height=0.25
    def assign(self,a,b,c,name1):
        self.color=a
        self.breed=b
        self.height=c
        self.name=name1
    def Walk(self,x):
        print(self.name , ' dog walk as'+x)
    def eat(self,x):
        print(self.name , ' dog is a'+x)
puppy=dog()
jimmy=dog()
puppy.assign('White','A',0.5,'Puppy')
jimmy.assign('Black','B',0.25,'Jimmy')
puppy.Walk('Slow')
jimmy.Walk('Fast')
puppy.eat('Veg')
jimmy.eat('NVeg')
