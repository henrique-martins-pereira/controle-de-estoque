import json

print("CONTROLE DE ESTOQUE")
print("-"*19)

try:
    with open ("estoque.json", "r", encoding="utf-8") as arquivo:
        estoque=json.load(arquivo)["estoque"]
except (FileNotFoundError, json.JSONDecodeError):
    estoque = 0

while True:
    print(" "*30)
    print("1. Adicionar \n2. Retirar \n3. Ver estoque \n4. SAIR")
    opc = int(input("Escolha o número desejado: "))
    if opc == 1:
        print("ADICIONAR AO ESTOQUE")
        print("-"* 20)
        add = int(input("Escolha o valor que deseja adicionar: "))
        estoque = estoque + add
        with open("estoque.json", "w", encoding = "utf-8") as arquivo:
            json.dump({"estoque": estoque}, arquivo, indent=4)
        print(f"Estoque atual: {estoque}")

    elif opc == 2:
        print("RETIRAR DO ESTOQUE")
        print("-"*18)
        retirar = int(input("Escolha o valor desejado: "))
        while True:
            if retirar > estoque:
                print("Não tem estoque")
            else:
                estoque -= retirar
                with open("estoque.json", "w", encoding = "utf-8") as arquivo:
                    json.dump({"estoque": estoque}, arquivo, indent = 4)
                print(f"Estoque atual: {estoque}")
                break

    elif opc == 3:
        print("VER ESTOQUE")
        print("-"* 11)
        print(f"Estoque atual: {estoque}")
        
    elif opc == 4:
        print("Saindo...")
        break
    else:
        print("Opção não encontrada!")
