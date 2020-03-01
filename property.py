class person:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    def delname(self):
        print('delname() called')
        del self.__name
    name=property(getname, setname,delname)
p=person()
p.name='Steve'
print(p.name)
del p.name

