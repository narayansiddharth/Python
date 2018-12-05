"""
Using data insurance.csv
(i) find the significant variable for predicting insurance charges .
Explain the model used
(ii) Plot the curves with your comments on each plot
(ii)develop a model for predicting insurance charges with input variables from the table.
"""

# Importing Python modules

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# from statsmodels.regression import linear_model

insuranceDataSet = pd.read_csv("insurance.csv")

# Get Column Names to list
insuranceSheetColumns: object = insuranceDataSet.columns.values.tolist()
print(insuranceSheetColumns)
# Fill Missing Data
column: object
for column in insuranceSheetColumns:

    if column == "charges":
        continue
    plt.figure()
    print(f"Filling Missing Data For {column}")
    if insuranceDataSet[column].dtype != "object":
        insuranceDataSet[column] = insuranceDataSet[column].fillna(insuranceDataSet[column].mean())
    else:
        insuranceDataSet[column] = insuranceDataSet[column].fillna('')
        insuranceDataSet[column] = LabelEncoder().fit_transform(insuranceDataSet[column])
    print(f"Plotting the individual Column Data, ({column}) ")
    insuranceDataSet[column].value_counts().plot(kind='bar')
    plt.title(column)

# Preparing the input Data For Model
InsuranceInputDataColumns = insuranceSheetColumns[0:len(insuranceSheetColumns) - 1]
print(InsuranceInputDataColumns)
Xinput = insuranceDataSet[InsuranceInputDataColumns]
sc = StandardScaler()
xInput = sc.fit_transform(Xinput)
yInput = insuranceDataSet['charges']
xTrain, xTest, yTrain, yTest = train_test_split(xInput, yInput, test_size=0.7)

# Preparing Different Models

# First trying with linear Regression

regression = linear_model.LinearRegression()
regression = regression.fit(xTrain, yTrain)

# Display the plots
plt.show()
