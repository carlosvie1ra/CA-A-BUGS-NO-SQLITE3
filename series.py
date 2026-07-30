import sqlite3
 
def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    #O aluno tenta cadastrar uma série com id_escola = 999 (que não existe).
    #O sqlite aceita o cadastro mesmo assim. Oque esta faltando ativar?
    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
        (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()
# está faltando ativar o "cursor.execute("PRAGMA foreign_keys = ON")", esse comendo é preciso porque o banco passa a verificar se o valor da chave estrangeira realmente existe
# na tabela de referencia. Se não existir, ele lança o excption (sqlite3.IntegrityError), que no seu código será vista pelo except.

serie = input("Digite o nome de uma série: ")
escola = int(input("Digite o id da escola: "))
cadastrar_serie(serie, escola)

cadastrar_serie(nome_serie, id_escola)