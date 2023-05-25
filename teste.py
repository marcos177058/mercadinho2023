# pip install mysql-connector-python
import mysql.connector

# Função para criar a conexão com o banco de dados
def criar_conexao():
    return mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='seu_banco_de_dados'
    )

# Função para adicionar um fornecedor
def adicionar_fornecedor():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Obter os detalhes do fornecedor
    nome = input("Digite o nome do fornecedor: ")
    email = input("Digite o email do fornecedor: ")
    telefone = input("Digite o telefone do fornecedor: ")

    # Inserir o fornecedor na tabela
    consulta = "INSERT INTO Fornecedores (nome, email, telefone) VALUES (%s, %s, %s)"
    valores = (nome, email, telefone)
    cursor.execute(consulta, valores)

    # Confirmar a inserção dos dados
    conexao.commit()
    print("Fornecedor adicionado com sucesso!")

    # Fechar a conexão
    cursor.close()
    conexao.close()

# Função para remover um fornecedor
def remover_fornecedor():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Obter o ID do fornecedor a ser removido
    id_fornecedor = input("Digite o ID do fornecedor que deseja remover: ")

    # Remover o fornecedor da tabela
    consulta = "DELETE FROM Fornecedores WHERE id = %s"
    valor = (id_fornecedor,)
    cursor.execute(consulta, valor)

    # Confirmar a remoção dos dados
    conexao.commit()
    print("Fornecedor removido com sucesso!")

    # Fechar a conexão
    cursor.close()
    conexao.close()

# Função para editar os dados de um fornecedor
def editar_fornecedor():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Obter o ID do fornecedor a ser editado
    id_fornecedor = input("Digite o ID do fornecedor que deseja editar: ")

    # Obter os novos detalhes do fornecedor
    novo_nome = input("Digite o novo nome do fornecedor: ")
    novo_email = input("Digite o novo email do fornecedor: ")
    novo_telefone = input("Digite o novo telefone do fornecedor: ")

    # Atualizar os dados do fornecedor na tabela
    consulta = "UPDATE Fornecedores SET nome = %s, email = %s, telefone = %s WHERE id = %s"
    valores = (novo_nome, novo_email, novo_telefone, id_fornecedor)
    cursor.execute(consulta, valores)

    # Confirmar a atualização dos dados
    conexao.commit()
    print("Dados do fornecedor atualizados com sucesso!")

    # Fechar a conexão
    cursor.close()
    conexao.close()

# Função principal para mostrar o menu e obter a opção do usuário
def main():
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar fornecedor")
        print("2. Remover fornecedor")
        print("3. Editar dados do fornecedor")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            adicionar_fornecedor()
        elif opcao == "2":
            remover_fornecedor()
        elif opcao == "3":
            editar_fornecedor()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")

# Executar o programa
if __name__ == '__main__':
    main()

