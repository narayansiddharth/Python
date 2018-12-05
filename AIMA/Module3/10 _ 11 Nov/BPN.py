import numpy as np

X = [[0.4, -0.7, 0.1], [0.3, -0.5, 0.05], [0.6, 0.1, 0.3], [0.2, 0.4, 0.25], [0.1, -0.2, 0.12]]
X = np.matrix(X)
print(X)

V = [[0.1, 0.4], [-0.2, 0.2]]
V = np.matrix(V)
W = [[0.2], [-0.5]]
W = np.matrix(W)
alpha = 0.001
nu = 0.6
#  Iteration starts
for k in range(0, 5):
    print('---------------Iteration  No :', (k + 1))
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
    k1 = HI[0, 0]
    k2 = HI[1, 0]
    print('---Output of hidden layer HO  , after activation by sigmoid function-----')
    # HO = [[1/(1+np.exp(-k1))],[1/(1+np.exp(-k2))]]
    r1 = 1 / (1 + np.exp(-k1))
    r2 = 1 / (1 + np.exp(-k2))
    HO = [[r1], [r2]]
    HO = np.matrix(HO)
    print(HO)
    # HO=np.matrix[[r1],[r2]]
    # print(HO)
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
    print('--Error square--')
    print(Esquare)

    # Updating the coefficients V and W

    d = (TO - YO) * YO * (1 - YO)
    print('d= ', d)
    Z = np.matmul(HO, d)
    print(Z)

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
