import sqlite3

conn = sqlite3.connect('Estoque.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL
)
''')

conn.commit()

def adicionar_produto():
    print("ADICIONAR PRODUTO")
    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))

    cursor.execute("SELECT quantidade FROM estoque WHERE produto = ?", (produto,))
    resultado = cursor.fetchall()

    if resultado:
        cursor.execute("UPDATE estoque SET quantidade = quantidade + ? WHERE produto = ?", (quantidade, produto))
        print(f"Produto {produto} já existe. Estoque atualizado!")
    else:  
        cursor.execute("INSERT INTO estoque (produto, quantidade) VALUES (?,?)", (produto, quantidade))
        print(f"Produto {produto} adicionado com sucesso!")
    conn.commit()


def ver_estoque():
    print("VER ESTOQUE")
    cursor.execute("SELECT * FROM estoque")
    produtos = cursor.fetchall()
    if not produtos:
        print("Não tem produto no estoque!")
    else:
        for produto in produtos:
            print(f"ID: {produto[0]} | Produto: {produto[1]} | Quantidade: {produto[2]}")
    
def remover_estoque():
    print("REMOVER QUANTIDADE DO ESTOQUE")
    cursor.execute("SELECT * FROM estoque")
    produtos = cursor.fetchall()
    if produtos == 0:
        print("Não tem produto no estoque!")
    else:
        for produto in produtos:
            print(f"ID: {produto[0]} | Produto: {produto[1]} | Quantidade: {produto[2]}")
    id = int(input("ID: "))
    quantidade = int(input("Quantidade: "))
    cursor.execute("SELECT quantidade FROM estoque WHERE id = ?", (id,))
    produto = cursor.fetchone()
    if not produto:
        print("ID não encontrado!")
        return
    quantidade_atual = produto[0]
    if quantidade_atual < quantidade:
        print("Não tem esse valor no estoque!")
    else:
        cursor.execute("UPDATE estoque SET quantidade = quantidade - ? WHERE id = ?", (quantidade, id))
        conn.commit()
        print(f"Novo estoque: {quantidade_atual - quantidade}")

while True:
    print("-"*20)
    print('CONTROLE DE ESTOQUE')
    print('''
1. Adicionar Estoque
2. Remover Estoque
3. Ver Estoque
4. SAIR
''')

    opcao = int(input("Escolha o número da opção desejada: "))

    if opcao == 1:
        print("-"*20)
        adicionar_produto()
    elif opcao == 2:
        print("-"*20)
        remover_estoque()
    elif opcao == 3:
        print("-"*20)
        ver_estoque()
    elif opcao == 4:
        print("-"*20)
        print("Saindo...")
        break