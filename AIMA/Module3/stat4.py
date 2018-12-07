import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = np.array([-0.018, -0.008, 0.011, 0.017, -0.008, -0.002])
y = np.array([-0.006, -0.001, 0.015, 0.017, -0.0019, -0.005])
print(x.shape)
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print("Gradient =", gradient)
print("Intercept = ", intercept)

print("R-squared", r_value ** 2)
slope = gradient

print("p-value", p_value)
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label='fitted line')
plt.legend()
plt.show()
