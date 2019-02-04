"""
Using data insurance.csv
(i) find the significant variable for predicting insurance charges .
Explain the model used
(ii) Plot the curves with your comments on each plot
(ii)develop a model for predicting insurance charges with input variables from the table.
"""

# Importing Python modules
import warnings
from typing import Any, Union
from venv import logger

import numpy as np
import pandas as pd
import sklearn
import statsmodels.api as sm
from matplotlib import pyplot as plt
from numpy.core.multiarray import ndarray
from pandas import DataFrame
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 1000)  # or 1000
pd.set_option('display.max_rows', 1000)  # or 1000
pd.set_option('display.max_colwidth', 199)  # or 199
pd.set_option('display.expand_frame_repr', False)


def fill_missing_data_columns(dataSet):
    dataSet = pd.DataFrame(dataSet)
    dataSetColumns = dataSet.columns
    for column in dataSetColumns:
        if dataSet[column].dtype != "object":
            dataSet[column] = dataSet[column].fillna(insuranceDataSet[column].mean())
        else:
            dataSet[column] = dataSet[column].fillna('')
    return dataSet


def convert_categorical_data(dataSet):
    dataSetColumns = dataSet.columns
    for column in dataSetColumns:
        if dataSet[column].dtype == "object":
            dataSet[column] = LabelEncoder().fit_transform(dataSet[column])
    return dataSet


def standardise_data(dataSet, standardisationMethod=None):
    if standardisationMethod is None:
        sc = StandardScaler()
        dataSet = sc.fit_transform(dataSet)
        standardisationMethodName: str = sc.__class__.__name__

    if standardisationMethod == "Max":
        dataSetColumns = dataSet.columns
        columnLength = len(dataSetColumns)
        dataArray = np.array(dataSet)

        standardisationMethodName = standardisationMethod
        while columnLength > 0:
            columnLength -= 1
            dataArray[columnLength] = dataArray[columnLength] / np.max(dataArray[columnLength])

        dataSet = dataArray

    if standardisationMethod == "Mean":
        dataSetColumns = dataSet.columns
        columnLength = len(dataSetColumns)
        dataArray = np.array(dataSet)

        standardisationMethodName = standardisationMethod
        while columnLength > 0:
            columnLength -= 1
            dataArray[columnLength] = dataArray[columnLength] / np.mean(dataArray[columnLength])

        dataSet = dataArray
    return dataSet, standardisationMethodName


def plot_input_data_set(dataSet, title):
    dataSetColumns = dataSet.columns
    for column in dataSetColumns:
        plt.figure()
        dataSet[column].value_counts().plot(kind='bar')
        plt.title(title + " - " + column)


def plot_input_and_target_data(x, y, xlabel, ylabel, title):
    plt.figure()
    plt.scatter(x, y)
    plt.xlabel = xlabel
    plt.ylabel = ylabel
    plt.title(title)


def get_age_range(ageArray):
    age_min = ageArray.min()
    if int(age_min / 10) == 0:
        age_min = 0
    else:
        age_min = int(age_min / 10) * 10

    age_max = ageArray.max()
    if int(age_max / 10) == 0:
        age_max = 10
    else:
        age_max = (int(age_max / 10) + 2) * 10

    age_range = np.arange(start=age_min, stop=age_max, step=10)
    return age_range


def calculate_prediction_error(modelName: object, yTestPredict: object, yTestActual: object, yTrainPredict: object,
                               yTrainActual: object) -> object:
    """

    :type yTrainActual: object
    :type yTestPredict: object
    """

    error = 0
    # testAverageError = ""
    yTestPredict = np.array(yTestPredict)
    yTestActual = np.array(yTestActual)

    if len(yTestActual) == len(yTestPredict):
        for i in range(len(yTestActual)):
            try:
                error += float(abs((abs(yTestActual[i]) - abs(yTestPredict[i])) / yTestActual[i]))
            except KeyError:
                continue;

        testAverageError = error / len(yTestActual) * 100
    else:
        print("Model has not predicted all test data...!!!")

    error = 0
    # trainAverageError = ""
    yTrainPredict = np.array(yTrainPredict)
    yTrainActual = np.array(yTrainActual)
    if len(yTrainActual) == len(yTrainPredict):
        for i in range(len(yTrainActual)):

            try:
                error += float(abs((abs(yTrainActual[i]) - abs(yTrainPredict[i])) / yTrainActual[i]))
            except KeyError:
                continue;

        trainAverageError = error / len(yTrainActual) * 100
    else:
        print("Model has not predicted all test data...!!!")

    if standardisationMethodName == "":
        errorList = \
            pd.DataFrame(
                {
                    "modelName": [modelName],
                    "Test Average Error": [testAverageError],
                    "Test MAE": [sklearn.metrics.mean_absolute_error(yTestActual, yTestPredict)],
                    "Test RMSE": [np.sqrt(sklearn.metrics.mean_squared_error(yTestActual, yTestPredict))],
                    "Train Average Error": [trainAverageError],
                    "Train MAE": [sklearn.metrics.mean_absolute_error(yTrainActual, yTrainPredict)],
                    "Train RMSE": [np.sqrt(sklearn.metrics.mean_squared_error(yTrainActual, yTrainPredict))]

                }
            )
    else:
        errorList = \
            pd.DataFrame(
                {

                    "standardisation Method Name": [standardisationMethodName],
                    "modelName": [modelName],
                    "Test Average Error": [testAverageError],
                    "Test MAE": [sklearn.metrics.mean_absolute_error(yTestActual, yTestPredict)],
                    "Test RMSE": [np.sqrt(sklearn.metrics.mean_squared_error(yTestActual, yTestPredict))],
                    "Train Average Error": [trainAverageError],
                    "Train MAE": [sklearn.metrics.mean_absolute_error(yTrainActual, yTrainPredict)],
                    "Train RMSE": [np.sqrt(sklearn.metrics.mean_squared_error(yTrainActual, yTrainPredict))]

                }
            )

    return errorList


def sklearn_liner_model_regressions(xTrain, xTest, yTrain, yTest):
    modelForConsideration: DataFrame = pd.DataFrame()
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
            # linear_model.LogisticRegression()
            # ,linear_model.LogisticRegressionCV(),linear_model.logistic_regression_path(xTrain, yTrain), linear_model.orthogonal_mp(xTrain, yTrain), linear_model.orthogonal_mp_gram(), linear_model.ridge_regression()
        ]
    for model in LinerModels:
        modelName: str = model.__class__.__name__
        try:
            # print(f"Preparing Model {modelName}")
            if modelName == "LogisticRegression":
                model = linear_model.LogisticRegression(random_state=0)
            model.fit(xTrain, yTrain)
            yTrainPredict = model.predict(xTrain)
            yTestPredict = model.predict(xTest)
            errorList = calculate_prediction_error(modelName, yTestPredict, yTest, yTrainPredict, yTrain)

            if errorList["Test Average Error"][0] < 30 and errorList["Train Average Error"][0] < 30:
                try:
                    modelForConsideration = modelForConsideration.append(errorList)
                except (Exception) as e:
                    print(e)

        except (Exception, ArithmeticError) as e:
            print(f"Error occurred while preparing Model {modelName}")
    return modelForConsideration


def insurance_regression_analysis(input, target_column):
    input_columns = [column for column in input.columns if column != target_column]
    insurance_input_data = input[input_columns]
    insurance_target_data = input[target_column]
    xTrain, xTest, yTrain, yTest = train_test_split(insurance_input_data, insurance_target_data, test_size=0.2)
    # xInput = np.array(xTrain)
    # xInput = sm.add_constant(xTrain)
    model = sm.OLS(yTrain, xTrain).fit()
    try:
        # print(model.summary())
        yTrainPredict = model.predict(xTrain)
        yTestPredict = model.predict(xTest)
        rsquared = model.rsquared
        parameters = model.params
        # print(f"rsquared : {rsquared}")
        # print(f"Coefficient Parameters : {parameters}")
        errorList = calculate_prediction_error(model.__class__.__name__, yTestPredict, yTest, yTrainPredict, yTrain)
        errorList['rsquared'] = rsquared
        for coef in parameters.keys():
            errorList["coefficient_" + coef] = parameters[coef]
        # print(errorList)
    except (Exception) as e:
        print("Stack Trace :: {0}".format(logger.exception(e)))
    return errorList


insuranceDataSet = pd.read_csv("insurance.csv")
# Removing trailing/leading whitespaces from column name
insuranceDataSet.columns = insuranceDataSet.columns.str.strip()
# Create model DataFrame to store all possible models
standardisationMethodName: str = ""
# Get Column Names to list
insuranceSheetColumns: object = insuranceDataSet.columns.values.tolist()
print(f"Columns present in the insurance data {insuranceSheetColumns}")
insuranceInputDataColumns = insuranceSheetColumns[0:len(insuranceSheetColumns) - 1]
print(f"Input columns for regression {insuranceInputDataColumns}")

# plot the gender based insurance input vs charges
for column in insuranceDataSet.columns:
    if column != 'charges':
        plot_input_and_target_data(insuranceDataSet[column], insuranceDataSet['charges'], column,
                                   'charges',
                                   f"insurance input {column} vs charges")

columns_to_exclude = 'sex'
model_error_list = pd.DataFrame()
for column_values in insuranceDataSet[columns_to_exclude].unique():
    print(f" Column Values - {column_values}")
    # Select only one particular gender values
    insuranceModelDataSet = insuranceDataSet[insuranceDataSet[columns_to_exclude] == column_values]
    columns = [column for column in insuranceDataSet.columns if column != columns_to_exclude]
    insuranceModelDataSet = insuranceModelDataSet[columns]
    insuranceModelDataSet = insuranceModelDataSet.reset_index(drop=True)
    print(f"insurance Model Data Set Columns : {insuranceModelDataSet.columns}")

    age_range = get_age_range(insuranceModelDataSet['age'])
    age_min = age_range[0]
    for age_max in age_range[1:]:
        insuranceInputModelDataSet = insuranceModelDataSet[
            ((insuranceModelDataSet['age'] >= age_min) & (insuranceModelDataSet['age'] <= age_max))]
        columns = [column for column in insuranceInputModelDataSet.columns if column != 'age']
        insuranceInputModelDataSet = insuranceInputModelDataSet[columns]
        insuranceInputModelDataSet = insuranceInputModelDataSet.reset_index(drop=True)
        # Fill Missing Data
        insuranceInputModelDataSet = fill_missing_data_columns(insuranceInputModelDataSet)
        # Encode Categorical data
        insuranceInputModelDataSet = convert_categorical_data(insuranceInputModelDataSet)
        errorList = insurance_regression_analysis(insuranceInputModelDataSet, 'charges')
        errorList.insert(1, column='gender', value=column_values)
        errorList.insert(2, column='age_min', value=age_min)
        errorList.insert(3, column='age_max', value=age_max)
        model_error_list = model_error_list.append(errorList)
        # print(errorList)
        age_min = age_max

model_error_list = model_error_list.reset_index(drop=True)

print("Regression Model Error and R-Squared Value, and Coefficients ::")
print(model_error_list)

# liner models from sklearn
# Fill Missing Data
insuranceModelDataSet = fill_missing_data_columns(insuranceDataSet)
# Encode Categorical data
insuranceModelDataSet = convert_categorical_data(insuranceModelDataSet)

# plot the individual models
plot_input_data_set(insuranceModelDataSet, "Insurance Data Set")

# Preparing the input Data For Model
insuranceDataSetStandardised: Union[ndarray, Any]
insuranceDataSetStandardised, standardisationMethodName = standardise_data(
    insuranceModelDataSet[insuranceInputDataColumns], standardisationMethod="Max")
xInput = insuranceDataSetStandardised
yInput = insuranceModelDataSet['charges']
xTrain, xTest, yTrain, yTest = train_test_split(xInput, yInput, test_size=0.1)

# Preparing Different Models

# linear Regression models from sklearn
modelForConsideration = sklearn_liner_model_regressions(xTrain, xTest, yTrain, yTest)
modelForConsideration = modelForConsideration.reset_index(drop=True)

print("Liner Model Errors")
print(modelForConsideration)

# Display the plots
plt.show()
