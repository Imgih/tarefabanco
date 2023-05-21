import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'admin',
  'password': 'brasil123',
  'host': 'database-1.cpdhir0s1jfs.us-east-1.rds.amazonaws.com',
  'database': 'tribosnativasbrasileiras'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Fechar a conexão
conn.close()