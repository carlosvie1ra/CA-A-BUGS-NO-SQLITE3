import sqlite3
def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    # se o id_prof não existir, ocorre um Integrityerror.
    # Se o erro acontecer, o que ocorre com a linha conexao.close()?
    try:
        cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)",(nome, id_serie, id_prof))
        conexao.commit()
    except sqlite3.OperationalError:
        print("Id professor nao existe.")
    
    finally:
        conexao.close()
    # Se acontecer um erro antes dela ser executada, o conexao.close() não será executado e a conexão com o banco fica aberta.

nome = input("Digite o nome")
id_serie = int(input("Digite o id da serie: "))
id_prof = int(input("Digite o id do professor: "))
cadastrar_turma(nome, id_serie, id_prof)