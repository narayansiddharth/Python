import matplotlib.pyplot as plt
import numpy as np
import plotNN

# X=[[0.4,-0.7,0.1],[0.3,-0.5,0.05],[0.6,0.1,0.3],[0.2,0.4,0.25],[0.1,-0.2,0.12]]
# X=np.matrix(X)
# print(X)
# print('Shape of X :',X.shape)
dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]
HO = []
i = 0
dataset = np.matrix(dataset)
X = dataset
[ri, ci] = X.shape
# ni is the number of input neurons
ni = ci - 1
# nh1 = no hidden neurons
nh1 = 2
# nt = number of output neurons
nt = 1
V = np.random.rand(ni, nh1)
# V=[[0.1,0.4],[-0.2,0.2]]
# V=np.matrix(V)
# W= [[0.2],[-0.5]]
W = np.random.rand(nh1, nt)
# W=np.matrix(W)
alpha = 0.001
nu = 0.6
cnt = 0

ep = 10
tr = 10
ktr = ep * tr
ERS = np.zeros((ktr))
ERS = np.array(ERS)
for epoch in range(0, ep):
    #  Iteration starts
    for k in range(0, tr):
        print('-Epoch no      :', (epoch + 1), ',   Row no :', (k + 1))
        # Output of Input layer = Input to input layer ,no activation here .This is optional
        xo = X[k, 0:2]
        xo = xo.T
        print(xo)
        # Target output TO
        TO = X[k, 2]
        print('Target=', TO)
        print('--Initial weights are V and W--')
        print(V)
        print(W)
        # HI is the input to hidden layer
        print('---Input to hidden layer---')
        HI = np.matmul(V.T, xo)
        print(HI)
        HO = 1 / (1 + np.exp(-HI))
        print('---Output of hidden layer HO  , after activation by sigmoid function-----')
        print(HO)
        # Input to output layer
        print('---Input to output layer---')
        YI = np.matmul((W.T), HO)
        print(YI)
        print('--output of output layer  after activation')
        # output of output layer after activation function
        YO = (1 / (1 + np.exp(-YI)))
        print(YO)
        # Error in computed output YO and target output TO  E=(TO-YO)
        E = TO - YO
        Esquare = E * E
        print('--Error square :', Esquare)
        ERS[cnt] = Esquare
        cnt = cnt + 1
        # Updating the coefficients V and W
        d = (TO - YO) * YO * (1 - YO)
        print('d= ', d)
        Z = np.matmul(HO, d)
        print('Z:', Z)
        delW = alpha * W + nu * Z
        print('Change in W')
        print(delW)
        # Updating V (Coeeficient between input and hidden layer
        e = W * d
        print('e=', e)
        print('---')
        aa = e[0, 0] * HO[0, 0] * (1 - HO[0, 0])
        bb = e[1, 0] * HO[1, 0] * (1 - HO[1, 0])
        ds = [[aa], [bb]]
        ds = np.matrix(ds)
        print(ds)
        rr = np.matmul(xo, ds.T)
        print('rr=', rr)
        delV = alpha * V + nu * rr
        print('delV=', delV)
        # Final updated values of V and W after one iteration

        W = W + delW
        V = V + delV

        print('---Updated W----- ')
        print(W)
        print('Updated V-----')
        print(V)
        print('------Iteration ends ------------ ')
# One iteration ends
print('cnt = ', cnt)
tt = np.linspace(0, (cnt - 1), cnt)
print(' No of rows in dataset =', tr)
print("Epoch =", ep)
print('Error square = ', Esquare)
# print(ERS)
plt.figure()
plt.plot(tt, ERS)
network = plotNN.DrawNN([ni, nh1, nt])
ff = network.draw()

plt.show()
