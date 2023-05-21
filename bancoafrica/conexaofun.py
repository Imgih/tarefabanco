import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host='3.224.147.85',
    user='usuarioremoto',
    password='minhasenha',
    database='animaisnativos'
    )
        
    return mydb