# input('-----Read csv file-----')
import pandas as pd

a = pd.read_excel('Sal.xlsx')
print(a)

input('-----List first 5 records-----')
print(a.head())

input('-----Check a particular column type-----')

print(a['Salary'].dtype)

input('--------Check types for all the columns---')
print(a.dtypes)

input('---------Calculate mean value for each numeric column per each group---')
a_rank = a.groupby('Rank')
print(a_rank)
print(a_rank.mean())

input('----------Calculate mean salary for each professor rank-----------')
a_sub = a[a['Salary'] > 120000]

print(a_sub)

input('----------Select only those rows that contain female professors----')
a_f = a[a['Gender'] == 'Female']
print(a_f)

input('------------Select column salary--------------')
print(a['Salary'])

input('-----------Select multiple column-----------')
print(a[['Rank', 'Salary']])

input('-----------Select rows by their position-----')
print(a[2:10])

input('-------------Select rows by their labels---------')
print(a_sub.loc[10:20, ['Rank', 'Gender', 'Salary']])

input('---------Select rows by their labels-------------')
print(a_sub.iloc[2:10, [0, 3, 4, 5]])

input('-------------Create a new data frame from the original sorted by the column Salary----')
a_sorted = a.sort_values(by='Service')
print(a_sorted.head())

input('-------------Aggregation Functions in Pandas-----------------')
print(a[['Salary', 'Service']].agg(['min', 'mean', 'max']))
