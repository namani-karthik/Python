class Addition:
    def Add(self,fargs,*args):
        sum=fargs
        for x in args:
            sum=sum+x
        print('The Sum of given numbers is',sum)
t=Addition()
t.Add(1,2)
t.Add(1,2,3,4,5,6,7,8,9)
