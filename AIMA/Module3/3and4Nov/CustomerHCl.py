import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as shc
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering

customer_data = pd.read_csv('shopping_data.csv')
print(customer_data.shape)
dt = np.array(customer_data)
# print(dt[0:10,:])
print(customer_data.head())
print(customer_data.iloc[0:10, 0:5].values)

data = customer_data.iloc[0:15, 3:5].values
print('--Linkage Matrix-only 10 rows------')
link = shc.linkage(data, method='ward')
print(link[0:10, ])
plt.figure(figsize=(6, 4))
plt.title("Customer Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward'))

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
clt = cluster.fit_predict(data)
print('--Clusters formed by program-----')
print(cluster.fit_predict(data))
plt.figure(figsize=(6, 4))
plt.scatter(data[:, 0], data[:, 1], c=cluster.labels_, cmap='rainbow')

plt.show()
