import pandas as pd

df = pd.DataFrame({'A': ['high', 'medium', 'low'],
                   'B': [10, 20, 30]},
                  index=[0, 1, 2])
print(df)

print('-----Next Example----------')
s = pd.Series(["a", "b", "c", "a"], dtype="category")
print(s)
print('--------Next Example ------------')
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)
print('--------Next Example ------------')
cat = cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'])
print(cat)
print('--------Next Example ------------')
cat = cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'], ordered=True)
print(cat)
