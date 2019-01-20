'''

 2. Using the insurance.csv data develop a region wise cluster .You may use a suitable algorithm for clustering .Explain the result .

'''
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings('ignore')

insuranceDataSet = pd.read_csv("insurance.csv")
# Removing trailing/leading whitespaces from column name
insuranceDataSet.columns = insuranceDataSet.columns.str.strip()

# Get Column Names to list
insuranceSheetColumns: object = insuranceDataSet.columns.values.tolist()
print(f"Columns present in the insurance data {insuranceSheetColumns}")
insuranceInputDataColumns = []
for column in insuranceDataSet.columns:
    if column != 'region':
        insuranceInputDataColumns.append(column)

print(f"Input columns for regression {insuranceInputDataColumns}")

clusters = len(insuranceDataSet['region'].unique())

# Fill Missing Data
column: object
for column in insuranceSheetColumns:
    if insuranceDataSet[column].dtype != "object":
        insuranceDataSet[column] = insuranceDataSet[column].fillna(insuranceDataSet[column].mean())
    else:
        insuranceDataSet[column] = insuranceDataSet[column].dropna()
        insuranceDataSet[column] = LabelEncoder().fit_transform(insuranceDataSet[column])

# cluster_input_columns = list(itertools.combinations(insuranceInputDataColumns, 3))
# xInput = np.array(list(insuranceDataSet[insuranceInputDataColumns]))

xInput = np.concatenate((insuranceDataSet['age'], insuranceDataSet['charges']))
yInput = insuranceDataSet['region']

print(xInput.size)

xInput = xInput.reshape(int(xInput.size / 2), 2)
for columns in insuranceInputDataColumns:
    plt.figure()
    plt.scatter(insuranceDataSet[column], yInput, cmap='rainbow')

# Create KMeans object
kmeans = KMeans(init='k-means++', n_clusters=clusters, n_init=10)

# Train the KMeans clustering model
kmeans.fit(xInput)

print(kmeans.labels_)

print("Cluster Classification")
for k in range(len(kmeans.labels_)):
    print(xInput[k, 0], xInput[k, 1], kmeans.labels_[k])
plt.figure()
plt.scatter(xInput[:, 0], xInput[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.show()
