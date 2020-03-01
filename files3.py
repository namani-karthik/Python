import os,sys

fname=input('Enter the file name')
if(os.path.isfile(fname)):
    f=open(fname,'r')
else:
    print('File doesnot exist')
    sys.exit()


cl=cw=cc=0
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)

'''print('No of lines:',cl)
print('No of wors:', cw)
print('No of Characters:',cc)'''
    
    
