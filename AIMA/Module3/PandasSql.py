import pandas as pd
import pyodbc

df = pd.read_csv("GDPData.csv")
print(df.shape)
print(' Data frame       ')
print(df)
print('----print of df ends ------')
# another dataframe created with few selected data
df1 = df[['GDP', 'Agriculture', 'Industry', 'Service']]
print('Selected columns  Agriculture Industry Service only')
print(df1)
print('  ---- This data are inserted into SQL table dbo.SqlGDP which can be verified in SQL server')
#  --- Tranfer this data into sql table---------
connection = pyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                            "Server=ADMIN\SQLEXPRESS;"
                            "Database=DBPython;"
                            "Trusted_Connection=yes;"
                            "Integrated Security=false")
cursor = connection.cursor()
for index, row in df1.iterrows():
    cursor.execute("INSERT INTO dbo.SqlGDP([GDP],[Agriculture],[Industry],[Service]) VALUES(?, ?,?,?)", row['GDP'],
                   row['Agriculture'],
                   row['Industry'],
                   row['Service'])

connection.commit()
connection.close()
