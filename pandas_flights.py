import pandas as pd

df= pd.read_csv('E:\\Python\\Naresh_ex\\flights.csv')
airline_info=df.groupby(['AIRLINE','WEEKDAY']).agg({'DIST':['sum','mean'],'ARR_DELAY':['min','max']}).astype(int)                                               
print(airline_info.head(7))
