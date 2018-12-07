import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('GDPData.csv')
print('  ------Original data from GDPData--------')
print(df)
df1 = df[['GDP', 'Agriculture', 'Industry', 'Service']]
print('------cumulative sum of columns-------')
print(df1.cumsum())
print('----cumsum over-----')
dt = np.array(df1)
print('-----Data From second column-------------')
tt = dt[:, 0:4]
print(tt)
# tt is a numpy array with GDP,Agriculture,Industry,Service
tr = np.transpose(tt)
print(tr.shape, tr.dtype)
cr = np.corrcoef(tr)
print('----correlation coefficient--------')
print(cr)
df1.plot()
df1.plot.bar(stacked=True)
df2 = df[['GDP']]
df3 = df[['Agriculture']]
df4 = df[['Industry']]
df2.plot.hist()
df3.plot.hist()
df4.plot.hist()
df1.plot.hist(stacked=True, bins=20)
# The first quartile (Q1) is defined as the middle number between the smallest number and the median of the data set.
#  The second quartile (Q2) is the median of the data.
# The third quartile (Q3) is the middle value between the median and the highest value of the data set.
df1.plot.box()
plt.show()
