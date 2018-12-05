import pypyodbc

connection = pypyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                              "Server=localhost;"
                              "Database=DBPython;"
                              "Trusted_Connection=yes;")
cursor = connection.cursor()
SQLCommand = (" INSERT INTO tr1 "
              "(Name,Rollno,English,Hindi,GK)"
              " VALUES(?,?,?,?,?)")
VALUES = ['Susan', 'E321', '55', '44', '50']
cursor.execute(SQLCommand, VALUES)
cursor.execute('SELECT * FROM tr1')
for row in cursor:
    print('row = %r' % (row,))
connection.commit()
connection.close()
