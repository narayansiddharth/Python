# Use GDP.csv data. Develop a multi regression analysis taking three significant variables

import itertools
from logging import exception

import numpy as np
import pandas as pd
import statsmodels.api as sm

# filePath: str = "C:/Python/AIMA/File/GDP.csv"

gdpDataSet = pd.read_csv("GDP.csv")

gdpDataSetList = [gdpDataSet.fillna(0), gdpDataSet.fillna(gdpDataSet.min()),
                  gdpDataSet.fillna(gdpDataSet.mean())]

for gdpDataSet in gdpDataSetList:
    Y = gdpDataSet['GDP']
    regressionVariableArray = list(
        itertools.combinations(['Agriculture', 'Industry', 'Service', 'Mining &Querying', 'Manufacturing'], 3))
    for r in regressionVariableArray:
        X = np.array(gdpDataSet[[r[0]] + [r[1]] + [r[2]]])
        X = sm.add_constant(X)
        model = sm.OLS(Y, X).fit()
        try:  # Exceptionis occurring while printing model summary and predict value, Not able to solve the exception till now
            print("Model Prepared using varaibles :: {0}".format(r))
            print(model.summary())
            print(model.predict(X))
        except exception as e:
            print("Error Occurred for :: {0}".format(r))
            print("Stack Trace :: {0}".format(e))
