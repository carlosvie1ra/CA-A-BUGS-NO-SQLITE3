import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Este bloco quebra ao rodar pela primeira vez em um banco limpo. Por quê?
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id_escola INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            )
        ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_serie TEXT,
        id_escola INTEGER,
        FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    ''')

        
    conexao.commit()
    conexao.close()
    #Ele quebra porque a cricação da tabela "series" possui uma chave estrangeira de uma tabela que será criada depois, então na criação da tabela series a variavel "id_escola" não tera referencia

    criar_tabelas()