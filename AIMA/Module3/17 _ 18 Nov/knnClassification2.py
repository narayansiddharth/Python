# Importing libraries
import operator

import numpy as np
import pandas as pd

#### Start of STEP 1
# Importing data 
data = pd.read_csv("HRA.csv")
dt = np.array(data)
#### End of STEP 1
print(data.head())


# Defining a function which calculates euclidean distance between two data points
def euclideanDistance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    return np.sqrt(distance)


# Defining our KNN model
def knn(trainingSet, testInstance, k):
    distances = {}
    sort = {}

    length = testInstance.shape[1]

    #### Start of STEP 3
    # Calculating euclidean distance between each row of training data and test data
    for x in range(len(trainingSet)):
        #### Start of STEP 3.1
        dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)

        distances[x] = dist[0]
        #### End of STEP 3.1

    #### Start of STEP 3.2
    # Sorting them on the basis of distance
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #### End of STEP 3.2

    neighbors = []

    #### Start of STEP 3.3
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    #### End of STEP 3.3
    classVotes = {}

    #### Start of STEP 3.4
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]

        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    #### End of STEP 3.4

    #### Start of STEP 3.5
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return (sortedVotes[0][0], neighbors)
    #### End of STEP 3.5


# Creating a dummy testset

testSet = [[27, 2, 0.270300158, 20, 3, 4, 6, 6, 3]]
testSet1 = [[50, 1, 0.518430753, 13, 0, 28, 20, 3, 3]]
test = pd.DataFrame(testSet)
print('    Test data ')
print(test)
#### Start of STEP 2
# Setting number of neighbors = 1
k = 1
#### End of STEP 2
# Running KNN model
result, neigh = knn(data, test, k)

# Predicted class
print(result)

# Nearest neighbor
print(neigh)
# Setting number of neighbors = 3 
k = 3
# Running KNN model 
result, neigh = knn(data, test, k)
# Predicted class 
print(result)
# 3 nearest neighbors
print(neigh)
# Setting number of neighbors = 5
k = 11
# Running KNN model 
result, neigh = knn(data, test, k)
# Predicted class 
print(result)
# 5 nearest neighbors
print(neigh)
# _------------- K = 5 --------------
nb1 = neigh[1]
print('---output from file')
print(dt[nb1, 9])
