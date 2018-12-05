import matplotlib.pyplot as plt
import neurolab as nl
import numpy as np
import plotNN

# Generate some training data
min_val = -10
max_val = 10
num_points = 120
x = np.linspace(min_val, max_val, num_points)
t = np.linspace(min_val, max_val, 30)
y = 3 * np.square(x) + 5
y /= np.linalg.norm(y)

y = y[0:30]
# Create data(input)  and labels(output) in 4 parts 30 each
data = x.reshape(30, 4)
print('-----Data----')
print(data)
labels = y.reshape(30, 1)
print('----Output-----')
print(labels)
print('-------------------')
z3 = labels.reshape(30, 1)
# Plot input data
plt.figure()
plt.scatter(data[:, 0], z3)
plt.scatter(data[:, 1], z3)
plt.scatter(data[:, 2], z3)
plt.scatter(data[:, 3], z3)
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Input data')

# Define a multilayer neural network with 2 hidden layers;
# First hid6den layer consists of 10 neurons
nh1 = 6
# Second hidden layer consists of 6 neurons
nh2 = 4
# Output layer consists of 1 neuron
nt = 1
# no of input neurons
mm = data.shape
ni = mm[1]
nn = nl.net.newff([[min_val, max_val], [min_val, max_val], [min_val, max_val], [min_val, max_val]], [nh1, nh2, nt])

# Set the training algorithm to gradient descent
nn.trainf = nl.train.train_gd

# Train the neural network
error_progress = nn.train(data, labels, epochs=2000, show=100, goal=0.01)
print("Minimum Value of Error")
print(min(error_progress))
# Plot training error
plt.figure()
plt.plot(error_progress)
plt.xlabel('Number of epochs')
plt.ylabel('Error')
plt.title('Training error progress')
# Run the neural network on training datapoints
output = nn.sim(data)
# y_pred = output.reshape(30)
plt.figure()
plt.plot(t, output, '-', t, z3, '.')
# The converged result is not satisfactory with the generated data
# Plot the output
# x_dense = np.linspace(min_val, max_val, num_points )
# y_dense_pred = nn.sim(x_dense.reshape(x_dense.size,1)).reshape(x_dense.size)

# plt.figure()
# plt.plot(x_dense, y_dense_pred, '-', x, y, '.', x, y_pred, 'p')
# plt.title('Actual vs predicted')

# Prediction
bb = np.array([2, 3, 4, 5])
bb = bb.reshape(1, 4)
zz = nn.sim(bb)
print(' Inputs for prediction ')
print(bb)
print(' Predicted output')
print(zz)
# create and draw multilayer neural network
network = plotNN.DrawNN([ni, nh1, nh2, nt])
ff = network.draw()
plt.show()
