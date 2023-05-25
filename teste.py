import sqlite3
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criação de uma tabela:
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')
# Inserção de dados em uma tabela:
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', ('João', 25))
# Consulta de dados em uma tabela:
cursor.execute('SELECT * FROM usuarios')
rows = cursor.fetchall()
for row in rows:
    print(row)
# Atualização de dados em uma tabela:
cursor.execute('UPDATE usuarios SET idade = ? WHERE id = ?', (30, 1))
# Exclusão de dados em uma tabela:
cursor.execute('DELETE FROM usuarios WHERE id = ?', (1,))
# Após executar todas as operações necessárias, não se esqueça de fazer o commit das alterações e fechar a conexão:
conn.commit()
conn.close()
