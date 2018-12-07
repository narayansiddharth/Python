import numpy as np
import pandas as pd
import statsmodels.api as sm

dt = pd.read_csv('XYData.csv')
npdt = np.array(dt)
a = npdt[:, 0]
b = npdt[:, 1]
print(npdt[:, 0])
ones = np.ones(len(a))
xval = a
# Addin column of 1 in xval
X = np.column_stack((xval, ones))
print(X)
# The augmented matrix is X
# Result by using OLS function of statmodels
print(" Linear Regression by using OLS function ")
results = sm.OLS(b, X).fit()
print(results.summary())
