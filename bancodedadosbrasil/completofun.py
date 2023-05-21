from conexaofun import conectar
from atualizar import editar1
from atualizar import editar2
from atualizar import editar3
from atualizar import editar4
from atualizar import editar5
from atualizar import editar6

def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tribosnativas")

    # Obter os resultados
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for resultado in resultados:
        print(resultado)

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def inserir(cod_tribo,nome_tribo,numero_hab,renda_mediasal, escolariedade, trabalho_asalariado):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para inserir um novo registro
    sql = "INSERT INTO tribosnativas (cod_tribo, nome_tribo, numero_hab, renda_mediasal, escolariedade, trabalho_asalariado) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (cod_tribo,nome_tribo,numero_hab,renda_mediasal, escolariedade, trabalho_asalariado)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Imprimir mensagem de sucesso
    print("Registro inserido com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
  

def deletar(cod_tribo):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM tribosnativas WHERE cod_tribo = %s"
    val = (cod_tribo,)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()



# chama a função conectar
conn = conectar()
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
while True:
  # Mostra as opções de operação
  print("O que você deseja fazer?")
  print("1 - Listar tribos")
  print("2 - Inserir nova tribo")
  print("3 - Editar uma tribo")
  print("4 - Deletar uma tribo")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    # Listar estados
    listar(conn, cursor)
  
  elif opcao == 2:
    # Inserir novo estado
    cod_tribo = int(input("Digite o código da nova tribo: "))
    nome_tribo = input("Digite o nome da nova tribo: ")
    numero_hab = float(input("Digite o número de habitantes: "))
    renda_mediasal = float(input("Digite a renda média mensal: "))
    escolariedade = input("Digite o nível de escolariedade: ")
    trabalho_asalariado = input("Possui trabalho assalariado (sim/não): ")
    inserir(cod_tribo,nome_tribo,numero_hab,renda_mediasal, escolariedade, trabalho_asalariado)

  elif opcao == 3:
    print("O que deseja editar ? ")
    print("1 - codigo da tribo")
    print("2 - Nome da tribo")
    print("3 - Número de habitantes")
    print("4 - Renda Media salarial")
    print("5 - Escolariedade")
    print("6-Trabalho Assalariado ")
    
    opcao = int(input("Digite o número da opção desejada: "))
     
    if opcao == 1:
        nome = input("Digite o nome da tribo que deseja editar: ")
        codigo = input("Digite o novo codigo da tribo: ")
        editar1(nome, codigo)
    elif opcao ==2:
        codigo = int(input("Digite o codigo da tribo que deseja editar: "))
        nome = input("Digite o novo nome da tribo: ")
        editar2(codigo, nome)
    elif opcao == 3:
        codigo = int(input("Digite o codigo da tribo que deseja editar: "))
        numero = float(input("Digite o novo número de habitantes da tribo: "))
        editar3(codigo, numero)
    elif opcao == 4:
        codigo = int(input("Digite o codigo da tribo que deseja editar: "))
        renda = float(input("Digite a nova renda mensal  da tribo: "))
        editar4(codigo, renda)
    elif opcao == 5:
        codigo = int(input("Digite o codigo da tribo que deseja editar: "))
        escolariedade = input("Digite a novo grau de escolariedade  da tribo: ")
        editar5(codigo, escolariedade)
    elif opcao == 6:
        codigo = int(input("Digite o codigo da tribo que deseja editar: "))
        trabalho = input("Digite o status do trabalho assalariado  da tribo: ")
        editar6(codigo, trabalho)
    
  elif opcao == 4:
    # Deletar um estado
    codigo = int(input("Digite o código da tribo que deseja deletar: "))
    deletar(codigo)

  elif opcao == 0:
    # Sair do programa
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()