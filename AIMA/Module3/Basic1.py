import matplotlib.pyplot as plt
import numpy as np

# Numbers:
x = 3
print(type(x))  # Prints "<class 'int'>"
print(x)  # Prints "3"
print(x + 1)  # Addition; prints "4"
print(x - 1)  # Subtraction; prints "2"
print(x * 2)  # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y))  # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2)  # Prints "2.5 3.5 5.0 6.25"
# List operation
a = [1, 6, 3, 9, 2]
print(a)
# list concatenation
print('------List concatenation ---------------')
x = [1, 2, 3, 4]
y = [[10], [20], [30]]
print(x)
print(y)
print('x=', x, 'y=', y)
print(x + y)
print('------another example on list -------')
# Our first simple Numpy example deals with temperatures. Given is a list with values, e.g. temperatures in Celsius:
avalues = [12, 45, 'Rahul', 45, 'Annadurai']
print(avalues)
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
print(type(cvalues))
# We will turn our list "cvalues" into a one-dimensional numpy array:
C = np.array(cvalues)
print(C)
print(C * 9 / 5 + 32)
print(type(C))
# Strings operations
hello = 'hello'  # String literals can use single quotes
world = "world"  # or double quotes; it does not matter.
print(hello)  # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw12)  # prints "hello world 12"
plt.plot(C)
plt.show()
