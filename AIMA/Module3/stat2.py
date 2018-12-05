import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print('Our array is:')
print(a)
print('\n')

print('Applying mean() function:')
print(np.mean(a))
print('\n')

print('Applying mean() function along axis 0:')
print(np.mean(a, axis=0))
print('\n')

print('Applying mean() function along axis 1:')
print(np.mean(a, axis=1))

print('-------------Another example --------------------')
a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])

print('Our array is:')
print(a)
print('\n')
print('----Median-----')
print('Applying median() function:')
print(np.median(a))
print('\n')
print('Applying median() function along axis 0:')
print(np.median(a, axis=0))
print('\n')
print('Applying median() function along axis 1:')
print(np.median(a, axis=1))
print('----Standard deviation   std = sqrt(mean(abs(x - x.mean())**2)) ------')
b = np.array((1, 2, 3, 4))
print(b)
print(np.std(b))
print('----Correlation matrix------')
print(np.corrcoef(a))

d = [1, 4, 5, 2, 6]
g = [3, 1, 2, 8, 4]
print(np.corrcoef(d, g))
