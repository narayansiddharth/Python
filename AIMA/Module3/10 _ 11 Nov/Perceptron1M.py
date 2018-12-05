# Make a prediction with weights
# Make a prediction with weights
import matplotlib.pyplot as plt
import numpy as np


def predict(row, weights):
    activation = weights[0]
    for i in range(len(row) - 1):
        activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0


# test predictions
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
weights = [-0.1, 0.20653640140000007, -0.23418117710000003]
dt = np.array(dataset)
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x1 = dt[0:10, 0]
x2 = dt[0:10, 1]
y = dt[0:10, 2]
# activation = (w1 * X1) + (w2 * X2) + bias
# activation = (0.206 * X1) + (-0.234 * X2) + -0.1
print('-----Dataset----')
for r in dataset:
    print("inputs =", r[0:2], "       output=", r[2])

print("----Perceptron computation-----")
for row in dataset:
    prediction = predict(row, weights)
    print("Expected=%d, Predicted=%d" % (row[-1], prediction))
plt.figure()
plt.scatter(t, x1, color=['red'])
plt.scatter(t, x2, color=['blue'])
plt.show()
