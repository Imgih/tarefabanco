import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host='database-1.cpdhir0s1jfs.us-east-1.rds.amazonaws.com',
        user='admin',
        password='brasil123',
        database='tribosnativasbrasileiras'
        )
        
    return mydb