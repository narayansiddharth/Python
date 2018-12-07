import matplotlib.pyplot as plt
import neurolab as nl
import numpy as np
import pandas as pd
import plotNN

x = pd.read_csv("GDP.csv")
data = np.array(x)
# Preprocessing
data = np.delete(data, 0, 1)
data1 = pd.DataFrame(data)
print('---------GDP Data   with missing values-------------')
print(data1)
mean = data1.mean()

data2 = data1[0].fillna(6.14), data1[1].fillna(3.48), data1[2].fillna(6.11), data1[3].fillna(7.76), data1[4].fillna(
    1.46), data1[5].fillna(13.64)
data2 = np.array(data2)
data3 = pd.DataFrame(data2)
data3 = data3.transpose()
print('  ----Step 1 ----Missing value  Filled up data ----')
print(data3)

# Preprocessing By Interpolation()
# data4 = data1
# data4 = data4.interpolate()
# Normalization by max.()
data5 = data3 / data3.max(axis=0)
print('-----Step 2-----Normalized Data---------')
print(data5)

# Normalization by Function()
# x = np.array(data1)
# min_max_scaler = preprocessing.MinMaxScaler()
# x_scaled = min_max_scaler.fit_transform(x)
# data6 = pd.DataFrame(x_scaled)
# Model
data5 = np.array(data5)
input = data5[:, 1:6]
[mi, ni] = input.shape
print('No of input neurons  ni=', ni)
output = data5[:, 0:1]
[m0, n0] = output.shape
print('No of output neurons n0=', n0)
t = np.linspace(0, 4, 35)
print(t)
print('-----Visualization by plots  ------')
# Plot
plt.figure()
plt.scatter(input[:, 0], output, label='Agriculture')
plt.scatter(input[:, 1], output, label='Industry')
plt.scatter(input[:, 2], output, label='Service')
plt.scatter(input[:, 3], output, label='Mining')
plt.scatter(input[:, 4], output, label='Manufacturing')
plt.xlabel('GDP')
plt.ylabel('AG,ID,SV,Mining,Manf')
plt.title('Data')
plt.legend(loc='upper left')
plt.show()
# Neural Network
ni = len(data5)
[m, n] = data5.shape

nh1 = 6
nh2 = 4
nt = n0
nn = nl.net.newff([[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]], [nh1, nh2, n0])
# Traning
nn.trainf = nl.train.train_gd
# Train the Neural network
print(' ------Result of   Neural Network----------')
error = nn.train(input, output, epochs=1000, show=500, goal=0.01)
print("Minimum Values Of Error")
print(min(error))
# plot
plt.figure()
plt.plot(error)
plt.xlabel('Number of epochs')
plt.ylabel('Error')
plt.title('Training error progress')

# run the Neural network
opt = nn.sim(input)
ypd = output.reshape(35)
plt.figure()
plt.plot(t, ypd, '-', label='Obs output')
plt.plot(t, opt, '-', label='sim output')
plt.title('Observed output and Simulated output')
plt.legend(loc='upper left')
# create and draw multilayer neural network
# ni =no of input neurons,nh1=no of first hidden neurons ,nh2,nt = no of output neorons=n0


network = plotNN.DrawNN([5, nh1, nh2, 1])
ff = network.draw()

plt.show()
# Predict
a = 0.9
b = 4.5
c = 5.0
d = 2.0
g = 0.8
prd = np.array([a, b, c, d, g])
prd = prd.reshape(1, 5)
p = nn.sim(prd)
print("Predicted GDP")
print(p)
