import mysql.connector

database = mysql.connector.connect(
        host = 'localhost',
        user= 'root',
        password='Root@123',
        database='nirmal'
    )

 



cursorobject = database.cursor()

cursorobject.execute('create table userbloodgroup (name varchar(20), bloodgroup varchar(20), password varchar(20))')

print('done')
