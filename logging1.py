import logging
print(logging.__file__)
logging.basicConfig(filename='E:\\Python\\Naresh_ex\\NT1123.txt',level=logging.INFO)


def add(fargs,*args):
    count=0    
    sum=0
    for i in args:
        sum=sum+i
        count+=1
    print(sum+fargs)
    str='Call is made to this function with',count+1
    logging.info(str)
add(1,2,3)
add(1,2)
add(1,2,3,4,5)
add(32,343,54,65,767,8)
add(1,2,3,4,5,6,7)
'''import logging
logging.basicConfig(filename='mylog.txt',level=logging.CRITICAL)'''

logging.critical('There is a serious problem')
logging.error('This is a Error message')
print('Program execution is done')
