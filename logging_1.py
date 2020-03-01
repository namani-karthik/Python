import logging
logging.basicConfig(filename='E:/Python/Jan_25/log1.txt',level=logging.NOTSET)

logging.info('Entering into try Except block')
try:    
    a=10
    b=0
    print(a/b)
except ZeroDivisionError as e:
    logging.critical(e)
logging.info('Exiting out of try Except block')
print('Done')
