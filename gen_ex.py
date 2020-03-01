def decor(num):
    def inner():
        value=num()
        n=value
        Store_value=''
        if(value>0):
            while(value>0):
                if(value%10==0):
                    Store_value='Zero '+Store_value
                elif(value%10==1):
                    Store_value='One '+Store_value
                elif(value%10==2):
                    Store_value='Two '+Store_value
                elif(value%10==3):
                    Store_value='Three '+Store_value
                elif(value%10==4):
                    Store_value='Four '+Store_value
                elif(value%10==5):
                    Store_value='Five '+Store_value
                elif(value%10==6):
                    Store_value='Six '+Store_value
                elif(value%10==7):
                    Store_value='Seven '+Store_value
                elif(value%10==8):
                    Store_value='Eigth '+Store_value
                else:
                    Store_value=('Nine ')+Store_value
                value=value//10
        return Store_value
    return inner
@decor
def num():
    n=7945721
    print(n)
    return n
print(num())




                
