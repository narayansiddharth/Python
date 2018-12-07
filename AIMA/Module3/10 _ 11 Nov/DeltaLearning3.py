import matplotlib.pyplot as plt
import numpy as np
import plotNN

# Weights are random numbers
np.random.seed(10)
X = [[0.86, 0.7, 0.4], [1, 0.3, 1.1], [0.2, 0.3, 0.4], [0.9, 0.85, 0.79], [0.2, 0.1, 0.9]]
X = np.matrix(X)
T = [[0.8], [0.7], [0.3], [1.1], [0.1]]
T = np.matrix(T)
print(X)
print('---Target----')
print(T)
W = np.random.rand(3, 1)
# W = [[0],[0],[0]]
alph = 0.25
W = np.matrix(W)
W = np.float64(W)
print('--W---')
print(W)
ep = 20
cnt = 0
# tr is the number of rows in dataset
tr = 5
ktr = ep * tr
ERS = np.zeros((ktr))
ERS = np.array(ERS)
lb = ['Banana', 'Pear', 'Lemon', 'Strawberry', 'Green Apple']
print(lb[0])
for epoch in range(0, ep):
    print('--------------------------Epoch No :', (epoch + 1))
    for k in range(0, tr):
        print('---Iteration No :', (k + 1))
        print('Computation for Fruit  :', lb[k])
        print('--Input---')
        print(X[k, 0:3])
        th = np.matmul(X[k, 0:3], W)
        print('th=', th)
        YO = 1 / (1 + np.exp(-th))
        Y = np.round(YO)
        print('Y =', Y)
        e = T[k] - Y
        Esquare = e * e
        ERS[cnt] = Esquare
        cnt = cnt + 1

        print('T=', T[k])
        print('Error=', e)
        delW0 = alph * e * X[k, 0]
        delW1 = alph * e * X[k, 1]
        delW2 = alph * e * X[k, 2]
        print('--Change in Weights ---')

        print(delW0, delW1, delW2)

        W[0, 0] = W[0, 0] + delW0
        W[1, 0] = W[1, 0] + delW1
        W[2, 0] = W[2, 0] + delW2
        print('--Updated weights ----')

        print(W[0, 0], W[1, 0], W[2, 0])
print('---Iteration ends ---')
print(' No of rows in dataset =', tr)
print("Epoch =", ep)
print('Error square = ', Esquare)

tt = np.linspace(0, (cnt - 1), cnt)
plt.figure()
plt.plot(tt, ERS)
network = plotNN.DrawNN([5, 1, 1])
ff = network.draw()

plt.show()
