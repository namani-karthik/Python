def display(farg, **kwargs):
    print('first argument: ',farg)
    for x,y in kwargs.items():
        print('key={},value={}'.format(x,y))
display(5,rno=10)
print()
display(5,rno=10,name='India')
