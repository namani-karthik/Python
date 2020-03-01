class test(Exception):
    name=None
    def assign(self,x):
        self.name=x
        print('Inside Exception11 File, Class test, assign method')
    def display(self):
        if(self.name==None):
            raise test('Name cannot be None')
        print('Name:',self.name)
        print('Inside Exception11 File, Class test, assign display')

class test1(Exception):
    name=None
    def assign(self,x):
        self.name=x
        print('Inside Exception11 File, Class test1, assign method')
    def display(self):
        if(self.name==None):
            raise test('Name cannot be None')
        print('Name:',self.name)
        print('Inside Exception11 File, Class test, assign method')

