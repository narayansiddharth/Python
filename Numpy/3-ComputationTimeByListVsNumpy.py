import time

import numpy as np

arrayElementSize = 1000000

# Basic List Computation
basicList_1 = range(arrayElementSize)
basicList_2 = range(arrayElementSize)

startTime = time.time()
print("Basic List Addition Start Time : ", startTime)
# Add the above List
computedList = [(x, y) for x, y in zip(basicList_1, basicList_2)]

stopTime = time.time()

print('Basic List Addition Stop Time : ', stopTime)
# print("ComputedList : ", computedList)
print("Time Taken to Complete the Basic List Addition : ", (stopTime-startTime)*1000)
# Numpy Array Computation
numpyArray_1 = np.arange(arrayElementSize)
numpyArray_2 = np.arange(arrayElementSize)

startTime = time.time()
print("Numpy Array Addition Start Time : ", startTime)
# Add the above Numpy Array
computedArray = numpyArray_1 + numpyArray_2

stopTime = time.time()
print("Numpy Array Addition Stop Time : ", stopTime)
# print('Numpy Array Addition : ', computedArray)
print("Time Taken to Complete the Numpy Addition : ", ((stopTime-startTime)*1000))


