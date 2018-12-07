import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print('Data on GDP from 1950-51 to 2012 in different sectors in Rs Crores')
x = pd.read_csv("econ.csv", header=None)
x = pd.DataFrame(x)
# print(x.dtypes)
# kk=x['Services'].values.astype('float')
yy = x.iloc[1:11, 1]
zz = pd.to_numeric(yy)
print('------Reading csv file and conversion to pandas dataframe-------')
print('-------10 rows of  first column of data frame ')
print(zz)
print('-----pp----')
# y = zz.astype(int)
# 3 and 4 row is now filled with nan
x.iloc[3:5, 1] = np.nan
kk = x.iloc[1:11, 1]
print(kk)
kk = pd.to_numeric(kk, errors='coerce')
gg = kk
print('---pp after filling up missing by mean---')
tt = kk.fillna(kk.mean())
print(tt)
print('--pp after filling missing data by interpolation')
ss = gg.interpolate()
print(ss)
#  Normalization of Data
print('Normalization of data by a function=(x-min(x))/(max(x)-min(x))')
dd = pd.read_csv("econ.csv", header=None)
dat1 = dd.iloc[1:11, 1]
dat2 = pd.to_numeric(dat1, errors='coerce')
dt = dat2
dtmax, dtmin = dt.max(), dt.min()
dt = (dt - dtmin) / (dtmax - dtmin)
print(dt)
# division by maximum value
print('  Normalization by division by max value')
pt = dat2
bb = pt / pt.max(axis=0)
print(bb)

# Normalization of data in array
print('-------- Normalization of data in array---------------')
sd = np.array(dd)
sd1 = sd[:, 1:5]

# sdmax,sdmin = sd1.max(),sd1.min()
# sd1 = (sd1-sdmin)/(sdmax-sdmin)
print('  ------Data in array    5 columns -----')
with open("econ.csv", 'r') as f:
    data = list(csv.reader(f, delimiter=","))
gt = np.array(data)
xt = gt[1:64, 1:6]
print(xt)
zt = np.array(xt, dtype=np.float)

print('  zt with 5 columns- normalized by division by max value-----')
yt = zt / zt.max(axis=0)
print(yt)
y1 = np.linspace(0, 62, 63)

plt.figure()
plt.plot(y1, yt[:, 1], 'r*', label='GDP')
plt.plot(y1, yt[:, 2], 'g-', label='Allied Agriculture')
plt.plot(y1, yt[:, 3], 'b-', label='Agriculture')
plt.plot(y1, yt[:, 4], 'cyan', label='Industry')
plt.legend(loc='upper left')
plt.title('Data')
plt.show()

plt.figure()
plt.scatter(y1, yt[:, 1], label='GDP')
plt.scatter(y1, yt[:, 2], label='Allied Agriculture')
plt.scatter(y1, yt[:, 3], label='Agriculture')
plt.scatter(y1, yt[:, 4], label='Industry')
plt.legend(loc='upper left')
plt.title('Data')
plt.show()
