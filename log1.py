import logging
logging.basicConfig(filename='E:\\Python\\Naresh_ex\\NT1.txt',level=logging.NOTSET)
def add(fargs,*args):
    count=0    
    sum=0
    for i in args:
        sum=sum+i
        count+=1
    print(sum+fargs)
    str='Call is made to this function with',count+1
    logging.info(str)
    logging.critical(str)
    logging.error(str)
    logging.warning(str)
    logging.debug(str)
add(1,2,3)
add(1,2)
add(1,2,3,4,5)
add(32,343,54,65,767,8)
add(1,2,3,4,5,6,7)
