f1=open('e:\\DSC_0302.jpg','rb')
f2=open('e:\\MyBinaryfile.jpg','wb')
b=f1.read()
f2.write(b)
f1.close()
f2.close()