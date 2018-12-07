import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[5, 3], [10, 15], [15, 12], [24, 10], [30, 45],
              [85, 70], [71, 80], [60, 78], [55, 52], [80, 91], ])
plt.figure()
plt.scatter(X[:, 0], X[:, 1], label='True Position')
plt.xlabel('  X1   ')
plt.ylabel('  X2  ')
plt.title('Scatter plot of data with two cordinates')
plt.figure()
# 2 clusters
print('---- Kmeans with 2 clusters-----')
kmeans = KMeans(n_clusters=2)
yy = kmeans.fit(X)
print(' Kmeans Centers=')
print(yy.cluster_centers_)
print('-------Data Classification  ----')
for k in range(len(kmeans.labels_)):
    print(X[k, 0], X[k, 1], kmeans.labels_[k])

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.xlabel('  X1   ')
plt.ylabel('  X2  ')
plt.title('Scatter plot of 2 clusters')
plt.figure()

plt.show()
