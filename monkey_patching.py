import monk
def monkey_f(self):
    print('Inside the monkey function')


monk.A.fun()

monk.A.fun=monkey_f
monk.A().fun()
    
