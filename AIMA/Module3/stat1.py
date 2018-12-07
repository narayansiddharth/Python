import matplotlib.pyplot as plt
import numpy as np

aa = np.array(((10.00, 8.04), (8.00, 6.95), (13.00, 7.58), (9.00, 8.81), (11.00, 8.33),
               (14.00, 9.96), (6.00, 7.24), (4.00, 4.26), (12.00, 10.84), (7.00, 4.82), (5.00, 5.68)))

# print(aa)
# print(aa.shape)
print('---------  Mean ,Average, Std deviation ------------')
print(np.mean(aa, axis=0))
print(np.average(aa))
print(np.std(aa))
plt.figure()
x = aa[:, 0]
y = aa[:, 1]
print('----scatter plot----------')
plt.scatter(x, y)
plt.show()
