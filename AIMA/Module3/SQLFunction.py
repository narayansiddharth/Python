import pyodbc

connection = pyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                            "Server=ADMIN\SQLEXPRESS;"
                            "Database=DBPython;"
                            "Trusted_Connection=yes;")
cursor = connection.cursor()
print("-----Fetch Data from SQL Table and Count the No. of records in a Column------")
query1 = ('SELECT COUNT(GDP) FROM SqlGDP')
cursor.execute(query1)
rows1 = cursor.fetchall()

for row in rows1:
    print(row)
print("-----SUM of data in a Column------")
query2 = ('SELECT SUM(GDP) FROM SqlGDP')
cursor.execute(query2)
rows2 = cursor.fetchall()

for row in rows2:
    print(row)
print("-----Maximum Value in a Column------")
query3 = ('SELECT MAX (GDP) FROM SqlGDP')
cursor.execute(query3)
rows3 = cursor.fetchall()

for row in rows3:
    print(row)
print("-----Minimum Value in a Column------")
query4 = ('SELECT MIN (GDP) FROM SqlGDP')
cursor.execute(query4)
rows4 = cursor.fetchall()

for row in rows4:
    print(row)
print("-----Average Value of a Column------")
query5 = ('SELECT AVG (GDP) FROM SqlGDP')
cursor.execute(query5)
rows5 = cursor.fetchall()

for row in rows5:
    print(row)
connection.commit()
connection.close()
