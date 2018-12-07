import numpy as np

a = np.array([0, 1, 2, 3, 4, 5])
print(a)

print(a.ndim)

print(a.shape)
b = a.reshape((3, 2))
print(b)

# In this case, we have modified the value 2 to 77 in b, and we can immediately see
# the same change reflected in a as well. Keep that in mind whenever you need a true copy
c = a.reshape((3, 2)).copy()
print(c)

c[0][0] = -99
print(a)
print(c)

# Here, c and a are totally independent copies.
# Another big advantage of NumPy arrays is that the operations are propagated
# to the individual elements.
print(a * 2)

print(a ** 2)
# Contrast that to ordinary Python lists:
z = [1, 2, 3, 4, 5] * 2
print(z)

# Indexing
aa = np.array([2, 3, 4])
print(aa)
print(a[np.array([2, 3, 4])])
print(a > 4)
print(a[a > 4])

# This can also be used to trim outliers.
print(a[a > 4])
print(a)

# As this is a frequent use case, there is a special clip function for it, clipping the values
# at both ends of an interval with one function call as follows:
print(a.clip(0, 4))
