# Using the data GDP.csv compute three clusters using k-means algorithm
import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

regressionVariableArray = list(
    itertools.combinations(['Agriculture', 'Industry', 'Service', 'Mining &Querying', 'Manufacturing'], 2))

# regressionVariableArray = list(itertools.combinations( [ 'Agriculture', 'Industry' ], 2 ) )
gdpDataSet = pd.read_csv("GDP.csv")
gdpDataSet = gdpDataSet.fillna(0)

for r in regressionVariableArray:
    X = np.array(list(zip(gdpDataSet[r[0]], gdpDataSet[r[1]])))
    # Plot input data

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], marker='o', facecolors='none', edgecolors='black', s=80)
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title('Input GDP Data of {0} and {1} before Clustering'.format(r[0], r[1]))
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

    # With 3 clusters
    print('   Kmeans with 3 clusters----')
    kmeans = KMeans(n_clusters=3)
    yy = kmeans.fit(X)
    print('---Centers of clusters------')
    cluster_centers = kmeans.cluster_centers_
    print(cluster_centers)
    print(' Kmeans Centers')
    print(yy.cluster_centers_)

    print('-------Data Classification  ----')
    for k in range(len(kmeans.labels_)):
        print(X[k, 0], X[k, 1], kmeans.labels_[k])

    # Plot the centers of clusters
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow', )

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title('After Clustering')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

plt.show()
