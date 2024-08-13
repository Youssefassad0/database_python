import pyodbc

try:
    connection_string = (
        'DRIVER={SQL Server};'
        'Server=(local);'
        'Database=mastedr;'
        'Trusted_Connection=True;'
    )
    print('Connected to dbs')
except pyodbc.Error as e:
    print("Error while connecting to SQL Server", e)