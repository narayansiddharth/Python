import numpy as np
import pylab as plt
from sklearn import datasets
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.svm import SVR
from sklearn.utils import shuffle

# Load housing data
data = datasets.load_boston()
ddt = np.array(data.data)
print(data.feature_names)

# Shuffle the data
X, y = shuffle(data.data, data.target, random_state=7)

# Split the data into training and testing datasets
num_training = int(0.8 * len(X))
X_train, y_train = X[:num_training], y[:num_training]
X_test, y_test = X[num_training:], y[num_training:]

# Create Support Vector Regression model
sv_regressor = SVR(kernel='linear', C=1.0, epsilon=0.1)

# Train Support Vector Regressor
sv_regressor.fit(X_train, y_train)

# Evaluate performance of Support Vector Regressor
y_test_pred = sv_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_test_pred)
evs = explained_variance_score(y_test, y_test_pred)
print("\n#### Performance ####")
print("Mean squared error =", round(mse, 2))
print("Explained variance score =", round(evs, 2))

# Test the regressor on test datapoint
test_data = [3.7, 0, 18.4, 1, 0.87, 5.95, 91, 2.5052, 26, 666, 20.2, 351.34, 15.27]
print("\nPredicted price:", sv_regressor.predict([test_data])[0])

boston = datasets.load_boston()
x = np.array([np.concatenate((v, [1])) for v in boston.data])
y = boston.target
s, total_error, _, _ = np.linalg.lstsq(x, y)
print('s')
print(s)
rmse = np.sqrt(total_error[0] / len(x))
print('Residual: {}'.format(rmse))

plt.plot(np.dot(x, s), boston.target, 'ro')
plt.plot([0, 50], [0, 50], 'g-')
plt.xlabel('predicted')
plt.ylabel('real')

from sklearn.linear_model import LinearRegression

lr = LinearRegression(fit_intercept=True)
data = x
target = y
lr.fit(data, target)
p = np.array(map(lr.predict, data))

# p = p.ravel() # p is a (1,16087) array, we want to flatten it
# e = p-target # e is 'error': difference of prediction and reality
# total_sq_error = np.sum(e*e)
# rmse_train = np.sqrt(total_sq_error/len(p))
# print(rmse_train)
plt.show()
