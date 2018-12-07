import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial import distance_matrix

X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]
df = X
dist = pd.DataFrame(distance_matrix(df, df))
print('distance :')
print(dist)
Z = linkage(X, 'ward')
print('  Linkage with ward function---')
print(Z)
fig = plt.figure(figsize=(8, 4))
dn = dendrogram(Z)
plt.title('Dendogram with ward linkage')
# Single linkage
Z = linkage(X, 'single')
print('--Linkage---- with single')
print(Z)
fig = plt.figure(figsize=(8, 4))
dn = dendrogram(Z)
plt.title('Dendogram with single linkage')
plt.show()
