import pandas as pd
from scipy.spatial import distance_matrix

data = [[5, 7], [7, 3], [8, 1]]
ctys = ['Boston', 'Phoenix', 'New York']
df = pd.DataFrame(data, columns=['xcord', 'ycord'], index=ctys)
print('--------Data--------')
print(df)
dist = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
print('-------Distance Matrix------')
print(dist)
