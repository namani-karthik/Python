import Emp, pickle
f=open('e:\\emp.dat','rb')
while True:
    try:
        obj=pickle.load(f)
        obj.Emp.display()
        obj.Emp.disp()
    except EOFError:
        print('Reached end of File')
        break
f.close()
'''
e=Emp.Emp(12,'dsdas',343)
pickle.dump(e,f)
e=Emp.Emp(12,'dsdas',343)
pickle.dump(e,f)
e=Emp.Emp(12,'dsdas',343)
pickle.dump(e,f)
f.close'''

