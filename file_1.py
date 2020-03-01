f=open('E:\\Python\\Naresh_ex\\NT.txt','r')
'''print('Enter the string, press @ to stop')
while(str!='@'):
    str=input()
    f.write(str)'''
f.seek(10,0)
print(f.read(10))
f.close()
print('Done')
