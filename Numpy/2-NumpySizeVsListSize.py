import sys
import numpy as np

size = 1000

pythonList: range = range(size)

print(pythonList)
print("Size of Python List ", sys.getsizeof(pythonList)*len(pythonList))

numpyArray: object = np.arange(size)
print("Size of Python Numpy Array ", numpyArray.size * numpyArray.itemsize)