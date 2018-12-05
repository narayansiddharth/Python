import numpy as np

x = np.array([[1, 2, 3, 4]])
y = np.reshape(x, (4, 1))
print(x)

print('--------')
print(y)
b = np.broadcast_arrays(x, y)
print('-----first matrix stretched-----')
print(b[0])
print('----second matrix stretched -------')
print(b[1])
print('------x+y-----')

print(x + y)

# d = np.braodcast_arrays(x+y)
# More examples
from numpy.lib.stride_tricks import as_strided

x = np.arange(16)
y = as_strided(x, (7, 4), (8, 4))  # overlapped entries

X, Y = np.meshgrid(np.arange(2), np.arange(2))
print('--X--')
print(X)
print('----Y---')
print(Y)
print('-----X+Y----')
print(X + Y)
print('--------------')
x = np.array([0, 1])
y = np.array([0, 1, 2])
X, Y = np.meshgrid(x, y)
print('X=    ')
print(X)
print('y=    ')
print(Y)
print('X+Y=')
print(X + Y)
