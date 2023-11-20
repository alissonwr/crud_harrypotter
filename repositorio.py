import sqlite3

#Gerando um ID
def gerar_id():
   conn = sqlite3.connect("harry_potter.db")
   cursor = conn.cursor()
   cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = 'personagens'")
   next_id = cursor.fetchone()[0]
   return next_id + 1

#Criando um personagem
def criar_personagem(nome, descricao, casa, imagem):
    try:
        conn = sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO personagens (nome_personagem, descricao_personagem, casa_personagem, imagem_personagem) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, descricao, casa, imagem))
        personagem_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return personagem_id
    except Exception as ex:
        print(ex)
        return 0

#Atualizando um personagem
def atualizar_personagem(id:int, nome, descricao, casa, imagem):
    try:
        conn = sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome_personagem = ?, descricao_personagem = ?, casa_personagem = ?, imagem_personagem = ? WHERE id_personagem = ?"
        cursor.execute(sql_update, (nome, descricao, casa, imagem, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    
#Deletando um personagem
def remover_personagem(id:int):
    try:
      conn= sqlite3.connect("harry_potter.db")
      cursor = conn.cursor()
      sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
      cursor.execute(sql_delete, (id, ))
      conn.commit()
      conn.close()
      return True   
    except Exception as ex:
        print(ex)
        return False

#Retornando um único personagem
def retornar_personagem(id:int): 
    try:
        if id == 0:
            return gerar_id(), "", "", "", ""
        conn =sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()

        sql_select = "SELECT * FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, descricao, casa, imagem = cursor.fetchone()
        conn.close()
        return id, nome, descricao, casa, imagem
    except:
        return False

#Retornando todos os personagens
def retornar_personagens():
    try:
        conn = sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM personagens"
        cursor.execute(sql_select)
        personagens = cursor.fetchall()
        conn.close()
        return personagens
    except:
        return False
