class Addition1:
    def Add(self,fargs,*args):
        sum=0
        for x in args:
            sum=sum+x
        print('The Sum of given numbers is',sum+fargs+self)

