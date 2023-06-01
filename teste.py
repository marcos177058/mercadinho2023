import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('gerenciamento_fornecedores.db')
cursor = conn.cursor()

# Criando tabela de fornecedores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        endereco TEXT,
        contato TEXT
    )
''')

# Criando a janela principal
root = tk.Tk()
root.title("Tela Principal")
root.geometry("800x600")

# Variáveis globais para os campos de entrada
nome_entry = None
endereco_entry = None
contato_entry = None

# Função para cadastrar um fornecedor
def cadastrar_fornecedor():
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    contato = contato_entry.get()

    cursor.execute('INSERT INTO fornecedores (nome, endereco, contato) VALUES (?, ?, ?)', (nome, endereco, contato))
    conn.commit()

    messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")

# Função para abrir uma nova janela com a lista de fornecedores
def ver_fornecedores_cadastrados():
    fornecedores_window = tk.Toplevel(root)
    fornecedores_window.title("Fornecedores Cadastrados")

    # Criando um widget de lista para exibir os fornecedores
    fornecedores_listbox = tk.Listbox(fornecedores_window, width=100)
    fornecedores_listbox.pack()

    # Consulta ao banco de dados para obter os fornecedores cadastrados
    cursor.execute('SELECT * FROM fornecedores')
    fornecedores = cursor.fetchall()

    # Adicionando os fornecedores à lista
    for fornecedor in fornecedores:
        fornecedores_listbox.insert(tk.END, f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Endereço: {fornecedor[2]}, Contato: {fornecedor[3]}")

# Função para abrir a janela de gerenciamento de fornecedores
def abrir_gerenciar_fornecedores():
    gerenciar_fornecedores_window = tk.Toplevel(root)
    gerenciar_fornecedores_window.title("Gerenciamento de Fornecedores")

    global nome_entry, endereco_entry, contato_entry

    # Criando os widgets da interface de gerenciamento de fornecedores
    nome_label = tk.Label(gerenciar_fornecedores_window, text="Nome:")
    nome_label.pack()
    nome_entry = tk.Entry(gerenciar_fornecedores_window)
    nome_entry.pack()

    endereco_label = tk.Label(gerenciar_fornecedores_window, text="Endereço:")
    endereco_label.pack()
    endereco_entry = tk.Entry(gerenciar_fornecedores_window)
    endereco_entry.pack()

    contato_label = tk.Label(gerenciar_fornecedores_window, text="Contato:")
    contato_label.pack()
    contato_entry = tk.Entry(gerenciar_fornecedores_window)
    contato_entry.pack()

    cadastrar_button = tk.Button(gerenciar_fornecedores_window, text="Cadastrar Fornecedor", command=cadastrar_fornecedor)
    cadastrar_button.pack()

    ver_fornecedores_button = tk.Button(gerenciar_fornecedores_window, text="Ver Fornecedores Cadastrados", command=ver_fornecedores_cadastrados)
    ver_fornecedores_button.pack()

    # Botão para voltar à tela principal
    voltar_button = tk.Button(gerenciar_fornecedores_window, text="Voltar", command=gerenciar_fornecedores_window.destroy)
    voltar_button.pack()

# Botão para acessar o gerenciamento de fornecedores
gerenciar_fornecedores_button = tk.Button(root, text="Gerenciar Fornecedores", command=abrir_gerenciar_fornecedores)
gerenciar_fornecedores_button.pack()

# Botão para acessar o cadastro de produtos
cadastro_produtos_button = tk.Button(root, text="Cadastro de Produtos")
cadastro_produtos_button.pack()

# Botão para acessar a visualização de estoque
visualizacao_estoque_button = tk.Button(root, text="Visualização de Estoque")
visualizacao_estoque_button.pack()

# Botão para acessar a criação de estoque
criacao_estoque_button = tk.Button(root, text="Criação de Estoque")
criacao_estoque_button.pack()

# Executando a interface
root.mainloop()

# Fechando a conexão com o banco de dados
conn.close()
