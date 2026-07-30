import sqlite3
def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    # 0 Python reclama de "Incorrect number of bindings".
    # Estamos passando a variável, por que ocorre o erro?
    cursor.execute("SELECT nome FROM professores WHERE id =?", (id_prof,))#"id_prof deve ter uma virgula depois porque é uma tupla com elemento"
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()


professor = int(input("Digite do id do professor: "))
buscar_professor(professor)