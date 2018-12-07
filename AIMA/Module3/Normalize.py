import numpy as np

x = np.array([1.5, 3.7, 2.6, 8.3, 5.65, 9.08, 2.2, 8.9, 1.9, 4.7])


def normalize():
    r = (x - min(x)) / (max(x) - min(x))
    return r


print('x Values     : ', x)
y = normalize()
print('Normalized  x :', y)
print('----Normalization by div by max value ------')


def norm():
    r = x / max(x)
    return r


print('x Values     : ', x)
y = norm()
print('Normalized  x :', y)
