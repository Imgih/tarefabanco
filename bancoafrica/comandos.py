from conexaofun import conectar
from editar import editar1
from editar import editar2
from editar import editar3
from editar import editar4
from editar import editar5


def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM especies")

    # Obter os resultados
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for resultado in resultados:
        print(resultado)

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def inserir(cod_espe,raca,quantidade,riscodeextincao, areaencontra):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para inserir um novo registro
    sql = "INSERT INTO especies (cod_espe, raca, quantidade, riscodeextincao, areaencontra) VALUES (%s, %s, %s, %s, %s)"
    val = (cod_espe,raca,quantidade,riscodeextincao, areaencontra)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Imprimir mensagem de sucesso
    print("Registro inserido com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def deletar(cod_espe):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM especies WHERE cod_espe = %s"
    val = (cod_espe,)
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




conn = conectar()
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
while True:
  # Mostra as opções de operação
  print("O que você deseja fazer?")
  print("1 - Listar especies nativas")
  print("2 - Inserir nova especie")
  print("3 - Editar uma especie")
  print("4 - Deletar uma especie")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    # Listar estados
    listar(conn, cursor)
  
  elif opcao == 2:
    # Inserir novo estado
    cod_espe = int(input("Digite o código da nova especie: "))
    raca = input("Digite o nome da nova raça: ")
    quantidade = int(input("Digite o número de especies vivas : "))
    riscodeextincao = input("A especie está em risco de extinção ? (sim ou não): ")
    areaencontra = input("Digite a área que encontra esta especie(norte,sul,oeste,leste) : ")
    inserir(cod_espe,raca,quantidade,riscodeextincao, areaencontra)
    
    
    
  elif opcao == 3:
    print("O que deseja editar ? ")
    print("1 - codigo da especie")
    print("2 - Nome da raça")
    print("3 - Número de animais da especie vivos")
    print("4 - Opção do risco de exentição")
    print("5 - Área onde se encontra a especie")
  
    
    opcao = int(input("Digite o número da opção desejada: "))
     
    if opcao == 1:
        nome = input("Digite o nome da especie que deseja editar: ")
        codigo = input("Digite o novo codigo da especie: ")
        editar1(nome, codigo)
    elif opcao ==2:
        codigo = int(input("Digite o codigo da especie que deseja editar: "))
        nome = input("Digite o novo nome da especie: ")
        editar2(codigo, nome)
    elif opcao == 3:
        codigo = int(input("Digite o codigo da especie que deseja editar: "))
        numero = int(input("Digite o nova quantidade de animais da especie vivos: "))
        editar3(codigo, numero)
    elif opcao == 4:
        codigo = int(input("Digite o codigo da especie que deseja editar: "))
        extin = input("Digite a nova opção de risco de extinção:  ")
        editar4(codigo, extin)
    elif opcao == 5:
        codigo = int(input("Digite o especie da tribo que deseja editar: "))
        area = input("Digite a nova área que se encontra a espécie: ")
        editar5(codigo, area)
    else:
        print("Opção não encontrada")


  elif opcao == 4:
    # Deletar um estado
    codigo = int(input("Digite o código da especie que deseja deletar: "))
    deletar(codigo)

  elif opcao == 0:
    # Sair do programa
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()