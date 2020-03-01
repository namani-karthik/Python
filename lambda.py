#from functools import reduce
#l=[1,2,3,4,5,6,7,8,9,10]
import pdb
#print("Filter function output",list(filter(lambda x:x%2,l)))
#print("Map function output",list(map(lambda x:x%2,l)))

#print("Reduce function output",reduce(lambda x,y:x+y,l))

def func(arg, *args):
    for x in args:
        pdb.set_trace()
        print(x)
    print('First argument in the function defination is:',arg)
func('a','b','c','d','e','f','g','h')
