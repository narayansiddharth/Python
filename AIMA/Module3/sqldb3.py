import numpy as np
import pandas as pd
import pyodbc

connection = pyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                            "Server=localhost;"
                            "Database=DBPython;"
                            "Trusted_Connection=yes;")
cursor = connection.cursor()
query = 'SELECT * FROM tr1'
df = pd.read_sql(query, connection)
cursor.execute('SELECT * FROM tr1')
for row in cursor:
    print('row = %r' % (row,))

print('------Data Size-------------------')
print(df.shape)
xx = df.shape
cnt = xx[0]
print('----- ------Print    dataframe-------')
print(df)
tt = np.array(df)
tt[:, 5] = tt[:, 2] + tt[:, 3] + tt[:, 4]
print('-----Print Total-----------')
print(tt)
print('-----Total ends-----')
tt1 = pd.DataFrame(tt)
connection.commit()
connection.close()

# -----------------------------------------------
connStr = pyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                         "Server=localhost;"
                         "Database=DBPython;"
                         "Trusted_Connection=yes;")
query1 = "SELECT [Name],[Roll No.],[English],[Hindi],[GK],[Total] FROM TR2"
df1 = pd.DataFrame.to_sql(query1, connStr, con=cursor)
cursor = connStr.cursor()
# cnt is the number of rows in tt shown above
for index, r in cnt:
    cursor.execute("INSERT INTO dbo.TR2([Name],[Roll No.],[English],[Hindi],[GK],[Total]) "
                   "values(tt1(r,0),tt1(r,1),tt1(r,2),tt1(r,3),tt1(r,4),tt1(r,5))")

connStr.commit()
cursor.close()
connStr.close()
