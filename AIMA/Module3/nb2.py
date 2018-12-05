import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

# assigning predictor and target variables
# x= np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
# y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])
# Create a Gaussian Classifier
dt = pd.read_csv('HROct2018.csv')
print(dt.head())
hr = np.array(dt)
print(hr[0:5, 0:10])
y = hr[:, 1]
x = hr[:, 2:10]
input('Enter any key')

model = GaussianNB()
# Train the model using the training sets
zz = model.fit(x, y)
print(zz)
# Predict Output
# pin = np.array([30,3.85,28,0.82,97,0,2,7,0 ])
# pp= pin.reshape(9,1)
# predicted= model.predict(pin)
# print('Inputs are [30,3.85,28,0.82,97,0,2,7,0)]')


# print( 'predicted output = ',predicted)
