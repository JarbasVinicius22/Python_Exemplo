import sqlite3
import os

# Nome do arquivo do banco de dados
DB_NAME = "notas_alunos.db"

def conectar_bd():

    """Conecta ao banco de dados SQLite e retorna a conexão."""
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela_alunos(conn):
    """Cria a tabela 'alunos' se ela não existir."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nota REAL NOT NULL,
            status TEXT NOT NULL
        );
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")

def adicionar_aluno(conn):
    """Adiciona um novo aluno e sua nota ao banco de dados."""
    try:
        nome = input("Digite o nome do aluno: ")
        if not nome:
            print("O nome não pode ser vazio.")
            return

        nota_str = input("Digite a nota do aluno (ex: 8.5): ")
        nota = float(nota_str.replace(',', '.')) # Aceita tanto ponto quanto vírgula

        # Define o status com base na nota
        if nota >= 7.0:
            status = "Aprovado"
        else:
            status = "Reprovado"

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO alunos (nome, nota, status) VALUES (?, ?, ?)",
            (nome, nota, status)
        )
        conn.commit()
        print(f"\nAluno '{nome}' adicionado com sucesso! Status: {status}\n")

    except ValueError:
        print("\nErro: A nota deve ser um número válido. Tente novamente.\n")
    except sqlite3.Error as e:
        print(f"\nErro ao inserir dados: {e}\n")

def listar_alunos(conn):
    """Lista todos os alunos cadastrados no banco de dados."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, nota, status FROM alunos")
        alunos = cursor.fetchall()

        # Limpa o terminal para melhor visualização
        os.system('cls' if os.name == 'nt' else 'clear')

        print("--- Lista de Alunos ---")
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            # Imprime o cabeçalho da tabela
            print(f"{'ID':<5} | {'Nome':<25} | {'Nota':<10} | {'Status':<15}")
            print("-" * 60)
            # Itera e imprime os dados dos alunos
            for aluno in alunos:
                print(f"{aluno[0]:<5} | {aluno[1]:<25} | {aluno[2]:<10.2f} | {aluno[3]:<15}")
        print("-" * 60)
        input("Pressione Enter para continuar...")


    except sqlite3.Error as e:
        print(f"Erro ao consultar o banco de dados: {e}")

def main():
    """Função principal que gerencia o menu e a interação com o usuário."""
    conn = conectar_bd()
    if conn:
        criar_tabela_alunos(conn)
    else:
        return # Encerra se não conseguir conectar ao BD

    while True:
        # Limpa o terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n--- Sistema de Gerenciamento de Notas ---")
        print("1. Adicionar Aluno e Nota")
        print("2. Listar Alunos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_aluno(conn)
        elif escolha == '2':
            listar_alunos(conn)
        elif escolha == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

    # Fecha a conexão com o banco de dados ao sair
    if conn:
        conn.close()

if __name__ == "__main__":
    main()