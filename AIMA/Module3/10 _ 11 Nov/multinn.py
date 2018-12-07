import matplotlib.pyplot as plt
import neurolab as nl
import numpy as np

# Generate some training data
min_val = -10
max_val = 10
num_points = 120
x = np.linspace(min_val, max_val, num_points)
t = np.linspace(min_val, max_val, 30)
y = 3 * np.square(x) + 5
y /= np.linalg.norm(y)
y = y[0:30]
# Create data and labels
data = x.reshape(30, 4)
labels = y.reshape(30, 1)
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
# First hidden layer consists of 10 neurons
# Second hidden layer consists of 6 neurons
# Output layer consists of 1 neuron
nn = nl.net.newff([[min_val, max_val], [min_val, max_val], [min_val, max_val], [min_val, max_val]], [6, 4, 1])

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
y_pred = output.reshape(30)
plt.figure()
plt.plot(t, output, '-', t, z3, '.')

# Plot the output 
# x_dense = np.linspace(min_val, max_val, num_points )
# y_dense_pred = nn.sim(x_dense.reshape(x_dense.size,1)).reshape(x_dense.size)

# plt.figure()
# plt.plot(x_dense, y_dense_pred, '-', x, y, '.', x, y_pred, 'p')
# plt.title('Actual vs predicted')

plt.show()
