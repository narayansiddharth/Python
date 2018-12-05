import pandas as pd

# Our small data set
d = {'one': [1, 1, 1, 1, 1],
     'two': [2, 2, 2, 2, 2],
     'letter': ['a', 'a', 'b', 'b', 'c']}
print('-------Create dataframe and group by item-----')
# Create dataframe
df = pd.DataFrame(d)
print(df)

# Create group object
one = df.groupby('letter')

# Apply sum function
print(one.sum())

letterone = df.groupby(['letter', 'one']).sum()
print(letterone)
print('-------another example on grouping-----')
# Group by function
df3 = pd.DataFrame({'X': ['A', 'B', 'A', 'B'], 'Y': [1, 4, 3, 2]})
print(df3.groupby(['X']).get_group('A'))
