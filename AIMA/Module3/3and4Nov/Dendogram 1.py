import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial import distance_matrix

# %matplotlib inline
X = np.array([[1, 2],
              [2.5, 4.5],
              [2, 2],
              [4, 1.5],
              [4, 2.5]
              ])
print('X =')
print(X)
print('----Distance------')
df = X
dist = pd.DataFrame(distance_matrix(df, df))
print(dist.values)

labels = range(1, 6)
# labels=[1,2,3,4,5]
plt.figure(figsize=(5, 3))
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:, 0], X[:, 1], label='True Position')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
linked = linkage(X, 'single')
print('---Linkage----')
print(linked)
labelList = range(1, 6)

plt.figure(figsize=(5, 3))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=True)
plt.show()
