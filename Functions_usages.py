'''def func1():
    def func2():
        print('Hi')
    func2()

x=func1()
'''

'''
def display(msg):
    return 'Hi '+ msg
def message():
    return 'How are you'
print(display(message()))'''

def display():
    def message():
        return 'How are you'
    return message
x=display()
print(x())
