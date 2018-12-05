import pyodbc

connection = pyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                            "Server=ADMIN\SQLEXPRESS;"
                            "Database=DBPython;"
                            "Trusted_Connection=yes;")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# -------------------------------------------------------------------------

sqlquery1 = ("INSERT INTO customers" "(name, address)"  "VALUES ( 'Rajiv ' ,  'Gurugram')")
sqlquery2 = ("SELECT * FROM customers")
cursor.execute(sqlquery1)
cursor.execute(sqlquery2)
for row in cursor:
    print('row = %r' % (row,))
connection.commit()
connection.close()
