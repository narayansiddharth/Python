import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Reading value from keyboard
x = input('enter x')
y = input('enter y')
sum = int(x) + int(y)
print('sum of{0} and {1} is {2}'.format(x, y, sum))
#
# 1. Read data
with open("ddt.csv", 'r') as f:
    data = list(csv.reader(f, delimiter=","))
x = np.array(data)
y = x.reshape(3, 5)
print(x)
z = np.array(y, dtype=np.int)
print(z)
# 2.  Another method of reading a file
# It’s possible to use NumPy to directly read csv or other files into arrays
dd = np.genfromtxt("ddt2.csv", delimiter=",", dtype=np.int)
print("first array")
print(dd)
print(dd[0:2, 0:3])
print(dd[0:2, 1:4])
# Normalization by dividinthe column by its maximum value
ddnorm = dd / dd.max(axis=0)
print(ddnorm)
# 3. Another method of reading data from file
a = pd.read_csv("ddt3.csv", delimiter=",", header=None)
b = np.array(a)
print(b)
# Reading string
gdp = np.genfromtxt("Book1.csv", delimiter=",", dtype=str)
print(gdp)
print(gdp[2, 4])
print("Writing Name ")
print("Mr.  " + gdp[2, 4] + str(123))
# Read and Write
# import csv
x = open('data1.csv', 'r')
z = pd.read_csv(x, header=None)
print(z.shape)
zz = np.array(z)
print(zz[0:3, 0:3])
tt = open('data2.csv', 'w')
tt.write(str(zz[0:3, 0:3]))
# use of matplotlib
xx = [5, 6, 8, 10, 15]
print(' values of xx')
print(xx)
t = [0, 1, 2, 3, 4]
plt.figure()
plt.plot(t, xx)
plt.title('Plot of xx    vs     t ')
plt.show()
