import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# x=np.array([-0.018,-0.008,0.011,0.017,-0.008,-0.002])
# y=np.array([-0.006,-0.001,0.015,0.017,-0.0019,-0.005])
dt = pd.read_csv('XYData.csv')
npdt = np.array(dt)
x = npdt[:, 4]
y = npdt[:, 5]
# change the column [0,1] ,[2,3],[4,5] and [6,7]
print(x.shape)
print('x values   :', x)
print('y values   :', y)
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print('mean of x =', np.mean(x))
print('mean of y =', np.mean(y))
print("Gradient =", gradient)
print("Intercept = ", intercept)

print("R-squared", r_value ** 2)
slope = gradient

print("p-value", p_value)
plt.figure()
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label='fitted line')
plt.legend()
plt.show()
