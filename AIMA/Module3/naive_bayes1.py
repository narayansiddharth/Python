import numpy as np
from sklearn.naive_bayes import GaussianNB

# assigning predictor and target variables
x = np.array([[-3, 7], [1, 5], [1, 2], [-2, 0], [2, 3], [-4, 0], [-1, 1], [1, 1], [-2, 2], [2, 7], [-4, 1], [-2, 7]])
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])
# Create a Gaussian Classifier
model = GaussianNB()
# Train the model using the training sets
zz = model.fit(x, y)
print(zz)
# Predict Output

# predicted= model.predict([[5,6],[3,4]])
# print('Inputs are [[5,6],[3,4]]')
predicted = model.predict(x)
print(' y =               ', y)
print('predicted output = ', predicted)
