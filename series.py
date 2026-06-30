import sqlite3

conexao = sqlite3.connect('sistema_escola.db')

conexao.execute("PRAGMA foreign_keys = ON;")
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS serie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_serie TEXT NOT NULL,
    id_escola INTEGER,
    FOREIGN KEY (id_escola) REFERENCES escola(id)
)''')

def cadastrar_serie():
    try: 
        print("\n ==== REGISTRAR SERIES ====")
        nome_serie = input("Qual o nome da serie que voce deseja cadastrar?: ")
        id_escola = int(input("Qual o ID da escola?: ")) 

        comando_inserir = '''INSERT INTO serie (nome_serie, id_escola) VALUES (?, ?)'''
        cursor.execute(comando_inserir, (nome_serie, id_escola)) 
        
        conexao.commit()
        print("Série registrada com sucesso!")
        
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: Escola inexistente ou dados inválidos! ({e})")
    finally:
        conexao.close()