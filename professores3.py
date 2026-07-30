import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
    	# Existe um erro de digitação no comando SQL (INSERTO).  
    	# Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe? 
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    
    except sqlite3.IntegrityError: 
        print("Erro: Este CPF já está cadastrado no sistema!") 

    except sqlite3.Error:
        print("Erro no codigo, jumento")


    finally: 
        conexao.close() 

nome = input("Digite o nome do professor: ")
materia = input("Digite a materia do professor: ")
cpf = input("Digite o cpf do professor: ")
inserir_professor(nome, materia, cpf)