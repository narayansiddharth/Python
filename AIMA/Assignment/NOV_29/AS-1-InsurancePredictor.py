"""
Using data insurance.csv
(i) find the significant variable for predicting insurance charges .
Explain the model used
(ii) Plot the curves with your comments on each plot
(ii)develop a model for predicting insurance charges with input variables from the table.
"""

# Importing Python modules

import warnings

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

warnings.filterwarnings('ignore')

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
xTrain, xTest, yTrain, yTest = train_test_split(xInput, yInput, test_size=0.2)

# Preparing Different Models

# First trying with linear Regression
LinerModels = \
    [
        linear_model.ARDRegression(), linear_model.BayesianRidge(), linear_model.ElasticNet(),
        linear_model.ElasticNetCV(),
        linear_model.HuberRegressor(), linear_model.Lars(), linear_model.LarsCV(), linear_model.Lasso(),
        linear_model.LassoCV(), linear_model.LassoLars(), linear_model.LassoLarsCV(), linear_model.LassoLarsIC(),
        linear_model.LinearRegression(), linear_model.MultiTaskLasso(),
        linear_model.MultiTaskElasticNet(), linear_model.MultiTaskLassoCV(), linear_model.MultiTaskElasticNetCV(),
        linear_model.OrthogonalMatchingPursuit(),
        linear_model.OrthogonalMatchingPursuitCV(), linear_model.PassiveAggressiveClassifier(),
        linear_model.PassiveAggressiveRegressor(), linear_model.Perceptron(),
        linear_model.RANSACRegressor(), linear_model.Ridge(), linear_model.RidgeClassifier(),
        linear_model.RidgeClassifierCV(),
        linear_model.RidgeCV(), linear_model.SGDClassifier(), linear_model.SGDRegressor(),
        linear_model.TheilSenRegressor(),
        linear_model.enet_path(xTrain, yTrain),
        linear_model.lars_path(xTrain, yTrain), linear_model.lasso_path(xTrain, yTrain),
        # linear_model.LogisticRegression(),linear_model.LogisticRegressionCV(),linear_model.logistic_regression_path(xTrain, yTrain), linear_model.orthogonal_mp(xTrain, yTrain), linear_model.orthogonal_mp_gram(), linear_model.ridge_regression()
    ]
for model in LinerModels:
    modelName: str = model.__class__.__name__
    try:
        print(f"Preparing Model {modelName}")
        model.fit(xTrain, yTrain)
        yTrainPredict = model.predict(xTrain)
        yTestPredict = model.predict(xTest)

        error = 0
        for i in range(len(yTrain)):
            try:
                error += float(abs(yTrainPredict[i] - yTrain[i]) / yTrain[i])
                train_error_tree = error / len(yTrain) * 100
            except KeyError:
                continue;

        print(f"Linear Regression Model :: {modelName} error on Train Data = {train_error_tree} percent in {model}")

        error = 0
        for i in range(len(yTest)):
            try:
                error += float(abs(yTestPredict[i] - yTest[i]) / yTest[i])
                test_error_tree = error / len(yTest) * 100
            except KeyError:
                continue;
        print(f"Linear Regression Model :: {modelName} error on Test Data = {train_error_tree} percent in {model}")
    except (Exception, ArithmeticError) as e:
        print(f"Skipping Model Preparation for {modelName}")

# Display the plots
plt.show()
