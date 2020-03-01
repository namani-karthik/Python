def function_name(exp):
    p=0
    c=0
    s=0
    for i in exp:
        if(i in ('[','{','(',']','}',')')):
            if(i=='['):
                s+=1
            elif(i=='{'):
                c+=1
            elif(i=='('):
                p+=1
            elif(i==']'):
                s-=1
            elif(i=='}'):
                c-=1
            elif(i==')'):
                p-=1
            if(s==-1 or p==-1 or c==-1):
                return False
    if(s==0 and p==0 and c==0):
        return True
    if(s>=0 or p>=0 or c>=0):
        return False
print(function_name('{(())'))
