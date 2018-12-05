import pandas as pd
from scipy.spatial import distance_matrix

data = [[1, 2], [2.5, 4.5], [2, 2], [4, 1.5], [4, 2.5]]

ctys = ['A', 'B', 'C', 'D', 'E']
df = pd.DataFrame(data, columns=['xcord', 'ycord'], index=ctys)
print('--------Data--------')
print(df)
dist = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
print('-------Distance Matrix------')
print(dist)
# Another method using Numpy
