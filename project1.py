from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
print(df)
print(df.loc[0:3])

'''location=r'E:\Python\births.csv'
dataframe=pd.read_csv(location, names=['Names','Births'])
Sorted=dataframe.sort_values(['Births'],ascending=True)
print(Sorted)
#print(dataframe['Names'].Max())
#print(dataframe)
print('Done')

dataframe['Births'].plot()
MaxValue=dataframe['Births'].max()
MaxName=dataframe['Names'][dataframe['Births']==dataframe['Births'].max()].values
Text=str(MaxValue) + "-" + MaxName
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
print(dataframe[dataframe['Births'] == dataframe['Births'].max()])
dataframe.mean(numeric_only=True).plot(kind='bar')
dataframe.plot.area(1954,2015)
plt.show()

l=r'E:\Python Projects\Rainfall_Data\mncl_june.csv'
df=pd.read_csv(l)
plt.close('all')'''
