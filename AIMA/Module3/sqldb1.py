import pandas as pd
import pyodbc

connection = pyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                            "Server=ADMIN\SQLEXPRESS;"
                            "Database=DBPython;"
                            "Trusted_Connection=yes;")
cursor = connection.cursor()

# -------------------------------------------------------------------------
sqlquery1 = ("INSERT INTO trnew" "(name, address)"  "VALUES ( 'Vivek Sharma' ,  'Delhi')")
sqlquery2 = ("SELECT * FROM trnew")
cursor.execute(sqlquery1)
cursor.execute(sqlquery2)
for row in cursor:
    print('row = %r' % (row,))
connection.commit()

# ---Reading table in sql ,convert to pandas dataframe ---------------------------------------
query = 'SELECT * FROM trnew'
df = pd.read_sql(query, connection)
print(' Print out of  Dataframe ')
print(df)
# ----------------------------------------------------
connection.commit()
connection.close()
