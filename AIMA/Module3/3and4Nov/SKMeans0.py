import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1, 1], [1.5, 2], [3, 4],
              [5, 7], [3.5, 5], [4.5, 5], [3.5, 4.5]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

prd = kmeans.predict([[0, 0], [4, 4]])
print(prd)
print('---Centers----')
cnt = kmeans.cluster_centers_
print(cnt)
print('Kmeans Labels')
lb = kmeans.labels_
print(lb.shape)
print(kmeans.labels_)
for k in range(len(lb)):
    print(X[k, 0], X[k, 1], lb[k])
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.xlabel('  X1   ')
plt.ylabel('  X2  ')
plt.title('Scatter plot of 3 clusters')
plt.show()
