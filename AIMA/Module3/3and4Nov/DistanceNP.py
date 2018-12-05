print('----Distance between a and b using Numpy----')
from scipy.spatial import distance

a = (1, 2, 3, 6)
b = (4, 5, 6, 8)
dst = distance.euclidean(a, b)
print('a=', a)
print('b=', b)
print('Distance =', dst)
