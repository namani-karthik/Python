class dog():
    def talk(self):
        print('bark')
class human():
    def talk(self):
        print('Hi')
def obj_talk(obj):
    obj.talk()

x=dog()
y=human()

obj_talk(x)
obj_talk(y)
