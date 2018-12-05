import numpy as np

# NumPy - Broadcasting. The term broadcasting refers to the ability of NumPy to treat arrays of different shapes
# during arithmetic operations. Arithmetic operations on arrays are usually done on corresponding elements.
# If two arrays are of exactly the same shape, then these operations are smoothly performed.
x = np.arange(4)

xx = x.reshape(4, 1)

y = np.ones(5)
z = np.ones((3, 4))

print('shape of x :', x.shape)
print('shape of xx :,', xx.shape)
print('Shape of z :', z.shape)
print('xx=', xx)
print('z =', z)
print("xx+y")
print(xx + y)
print('----another example------')
a = np.array((0, 10, 20, 30))
print('a=', a)
b = np.array((0, 1, 2))
print('b=', b)
y = a[:, None] + b
print(a[:, None])
print('y=', y)
