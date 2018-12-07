import numpy as np

a = np.array([[2, 3, 4, 7], [5, 4, 3, 2], [6, 3, 2, 1], [8, 3, 4, 7]])
print(a)
input('----column slicing --------PE')
print(a[:, 1:3])
input('------Row slicing----------PE')
print(a[1:3, :])
