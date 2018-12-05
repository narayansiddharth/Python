import statsmodels.api as sm
from sklearn import datasets  ## imports datasets from scikit-learn

data = datasets.load_boston()
import pandas as pd

# define the data/predictors as the pre-set feature names
df = pd.DataFrame(data.data, columns=data.feature_names)

# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target, columns=["MEDV"])
## Without a constant
X = df["RM"]
y = target["MEDV"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X)  # make the predictions by the model

# Print out the statistics
print("Single input RM and single output MEDV")
print(model.summary())
# regression model with more than one variable 

X = df[['RM', 'LSTAT']]
y = target['MEDV']
model = sm.OLS(y, X).fit()
predictions = model.predict(X)
print("Two inputs RM and LSTAT and One output  MEDV")
# The summary gives the coefficients and the intercept,Rsquare  , y= c +ax1 +bx2
print(model.summary())
# Using data from sklearn and Linear_model
from sklearn import linear_model

# from sklearn import datasets ## imports datasets from scikit-learn done above
# data = datasets.load_boston() ## already done above
# define the data/predictors as the pre-set feature names
df = pd.DataFrame(data.data, columns=data.feature_names)

# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target, columns=['MEDV'])
X = df
y = target['MEDV']
lm = linear_model.LinearRegression()
model = lm.fit(X, y)
predictions = lm.predict(X)
# print(predictions)[0:5]
print(lm.score(X, y))
print(lm.coef_)
print(lm.intercept_)
