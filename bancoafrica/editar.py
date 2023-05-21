from conexaofun import conectar

def editar1(raca, ncod_espe):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE especies SET cod_espe = %s WHERE raca = %s"
    val = (ncod_espe, raca)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
def editar2(cod_espe, nraca):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE especies SET raca = %s WHERE cod_espe = %s"
    val = (nraca, cod_espe)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def editar3(cod_espe, nquantidade):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE especies SET quantidade = %s WHERE cod_espe = %s"
    val = (nquantidade, cod_espe)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
def editar4(cod_espe, nriscodeextincao):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE tribosnativas SET riscodeextincao = %s WHERE cod_espe = %s"
    val = (nriscodeextincao, cod_espe)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
    

def editar5(cod_espe, nareaencontra):
        conn = conectar()

     # Criando um objeto cursor para executar as consultas SQL
        cursor = conn.cursor()
        sql = "UPDATE tribosnativas SET areaencontra = %s WHERE cod_espe = %s"
        val = (nareaencontra, cod_espe)
        cursor.execute(sql, val)

    # Commit da transação
        conn.commit()

    # Verificar se algum registro foi atualizado
        if cursor.rowcount == 0:
         print("Nenhum registro atualizado.")
        else:
            print("Registro atualizado com sucesso.")

    # Fechar a conexão e o cursor
        cursor.close()
        conn.close()