import numpy as np

# Create Numpy Array
numpyArray = np.array([(1, 2, 3), (4, 5, 6)])

print("Numpy Array Data Type : ", numpyArray.dtype)
print("Numpy Array Dimension : ", numpyArray.ndim)
print("Numpy Array Item Size : ", numpyArray.itemsize)
print("Numpy Array Size : ", numpyArray.itemsize * numpyArray.size)
print("Numpy Array Shape : ", numpyArray.shape)
print("Numpy Array Re-shape : ", numpyArray.reshape(3, 2))
