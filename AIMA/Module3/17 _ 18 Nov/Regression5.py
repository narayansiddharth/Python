import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from numpy.linalg import inv

# Read driving experience ,de as input variable
de = [5, 2, 12, 9, 15, 6, 25, 16]
# Read autoinsurance ,ai as output variable
ai = [64, 87, 50, 71, 44, 56, 42, 60]

ones = np.ones(len(de))
xval = np.transpose(de)
print("Input variable")
print(xval)
print("Output Variable")
print(de)
# Addin column of 1 in xval
X = np.column_stack((xval, ones))
# The augmented matrix is X
# Result by using OLS function of statmodels
print(" Linear Regression by using OLS function ")
results = sm.OLS(ai, X).fit()
print(results.summary())
print("----regression by matrix inversion----")
# Regression by Matrix inversion
b = np.transpose(ai)
XT = np.transpose(X)
XTX = np.matmul(XT, X)
XTXInv = inv(XTX)
XX = np.matmul(XTXInv, XT)
A = np.matmul(XX, ai)
print("The coefficients are")
print("Intercept is ")
yc = A[1]
print(yc)
print(" The slope is ")
sl = A[0]
print(sl)
# Plot the best fit line
best_fit = []
for i in xval:
    best_fit.append(sl * i + yc)
plt.plot(xval, ai, 'o', label='Data')
plt.plot(xval, best_fit, 'r', label='Best fit Line', linewidth=3)
plt.legend(loc='upper left')
plt.show()
