from conexaofun import conectar

def editar1(nome_tribo, ncod_tribo):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE tribosnativas SET cod_tribo = %s WHERE nome_tribo = %s"
    val = (ncod_tribo, nome_tribo)
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
    
def editar2(cod_tribo, nnome_tribo):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE tribosnativas SET nome_tribo = %s WHERE cod_tribo = %s"
    val = (nnome_tribo, cod_tribo)
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


def editar3(cod_tribo, nnumero_hab):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE tribosnativas SET numero_hab = %s WHERE cod_tribo = %s"
    val = (nnumero_hab, cod_tribo)
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
    
def editar4(cod_tribo, nrenda_mediasal):
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    sql = "UPDATE tribosnativas SET renda_mediasal = %s WHERE cod_tribo = %s"
    val = (nrenda_mediasal, cod_tribo)
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
    
def editar5(cod_tribo, nescolariedade):
        conn = conectar()

     # Criando um objeto cursor para executar as consultas SQL
        cursor = conn.cursor()
        sql = "UPDATE tribosnativas SET escolariedade = %s WHERE cod_tribo = %s"
        val = (nescolariedade, cod_tribo)
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

def editar6(cod_tribo, ntrabalho_asalariado):
        conn = conectar()

     # Criando um objeto cursor para executar as consultas SQL
        cursor = conn.cursor()
        sql = "UPDATE tribosnativas SET trabalho_asalariado = %s WHERE cod_tribo = %s"
        val = (ntrabalho_asalariado, cod_tribo)
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