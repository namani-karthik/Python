f1=open('E:\\Naresh\\file\\AnnexureH.pdf','rb')
f2=open('E:\\Naresh\\file\\Surya1.pdf','wb')

f2.write(f1.read())

f1.close()
f2.close()

print('File coping is done')
