# pip install mysql-connector-python
import mysql.connector
# Dados da conexão
cnx = mysql.connector.connect(
    host='[seu_host]',
    user='[seu_usuario]',
    password='[sua_senha]',
    database='[seu_banco_de_dados]'
)
# Objeto para realizar consultas
cursor = cnx.cursor()
# Inserindo dados em uma tabela
query = "INSERT INTO nome_da_tabela (coluna1, coluna2) VALUES (%s, %s)"
values = ("valor1", "valor2")
cursor.execute(query, values)
# Confirmando alterações
cnx.commit()
# Finalizando interação com o banco de dados
cursor.close()
cnx.close()


