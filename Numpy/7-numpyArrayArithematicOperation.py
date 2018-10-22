import numpy as np
from numpy.core.multiarray import ndarray

numpyArray_1: ndarray = np.arange(10)

print(numpyArray_1)
print("Max numpyArray_1 : ", numpyArray_1.max())
print("Min numpyArray_1 : ", numpyArray_1.min())
print("Sum numpyArray_1 : ", numpyArray_1.sum())

numpyArray_2: ndarray = np.array([(np.arange(10)), (np.arange(10, 20))])

print(numpyArray_2)
print("Max numpyArray_2 : ", numpyArray_2.max())
print("Min numpyArray_2 : ", numpyArray_2.min())
print("Sum numpyArray_2 : ", numpyArray_2.sum())
print(numpyArray_2)
print("Sum numpyArray_2(axis=0) : ", numpyArray_2.sum(axis=0))
print("Sum numpyArray_2(axis=1) : ", numpyArray_2.sum(axis=1))
