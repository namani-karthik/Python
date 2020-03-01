from pandas import DataFrame, read_csv

#import matplotlib.pylot as plt
import pandas as pd
import sys
import matplotlib
names=['venkat','Vijaya','Karthik','Swetha','Gotham','Surya']
births=[1954,1956,1983,1989,2012,2015]

Baby_ds=list(zip(names,births))

df=pd.DataFrame(data=Baby_ds, columns=['Names','Birth'])

df.to_csv('births.csv',index=False,header=False)
print('Done')
