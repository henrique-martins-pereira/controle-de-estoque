print("CONTROLE DE ESTOQUE")
print("-"*19)

estoque = 2000
while True:
    print("-"*20)
    print("1. Adicionar \n2. Retirar \n3. Sair")
    opc = int(input("Escolha o número desejado: "))
    
    if opc == 1:
        print("ADICIONAR AO ESTOQUE")
        print("-"*20)
        
        add = int(input("Adicionar número ao estoque: "))
        estoque = estoque + add
        print(f"Estoque atual: {estoque}")
        
    elif opc == 2:
        while True:
            print("RETIRAR DO ESTOQUE")
            print("-"*18)
        
            retirar = int(input("Número desejado: "))
            if retirar > estoque:
                print("Não tem estoque")
            else:
                estoque = estoque - retirar
                print(f"Estoque atual: {estoque}")
                break
    elif opc == 3:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")