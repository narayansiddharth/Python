import numpy as np

X = [[1, 1, 0], [1, 0, 1], [0, 0, 0], [1, 1, 1], [0, 0, 1]]
X = np.matrix(X)
T = [[1], [1], [0], [1], [0]]
T = np.matrix(T)
print(X)
print('---Target----')
print(T)
W = [[0], [0], [0]]
alph = 0.25
W = np.matrix(W)
W = np.float64(W)
print('--W---')
print(W)
lb = ['Banana', 'Pear', 'Lemon', 'Strawberry', 'Green Apple']
print(lb[0])

print('---Iteration begins ')
for k in range(0, 5):
    print('---Iteration No :', (k + 1))
    print('Computation for Fruit  :', lb[k])
    print('--Input---')
    print(X[k, 0:3])
    th = np.matmul(X[k, 0:3], W)
    print('th=', th)
    if th < 0.4:
        Y = 0
    else:
        Y = 1
    print('Y =', Y)
    e = T[k] - Y
    print('T=', T[k])
    print('e=', e)
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
