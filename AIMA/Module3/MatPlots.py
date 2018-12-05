print("------------Plot Against Indices-------------")
import matplotlib.pyplot as plt
import numpy as np

pi = 22 / 7
x = np.arange(50) * 2 * pi / 50.
y = np.sin(x)
plt.xlabel('index')
plt.plot(y)
plt.show()
print("---------------MULTIPLE DATA SETS--------------")
plt.plot(x, y)
plt.xlabel('radians')
plt.show()
print("--------------Red, Dot-Dash, Triangles----------")
plt.plot(x, np.sin(x), 'r-^')
plt.show()
print("-------------------Scatter Plot------------------")
x = np.arange(50) * 2 * pi / 50.
y = np.sin(x)
plt.scatter(x, y)
plt.show()
print("-----------------Marker size/color set with data------------")
x = np.random.rand(200)
y = np.random.rand(200)
size = np.random.rand(200) * 30
color = np.random.rand(200)
plt.scatter(x, y, size, color)
plt.colorbar()
plt.show()
print("-----------------------------Histogram-------------------------")
plt.hist(np.random.rand(1000))
plt.show()
