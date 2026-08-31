numeros = {}

while True:
    print("[1] Adicionar numero.\n[2] Procurar numero.\n[3] Remover contato.\n[4] Sair")
    escolha = int(input("R: "))

    match escolha:
        case 1:
            contato = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone: ")
            numeros[contato] = telefone
        case 2:
            procurar_contato = input("Digite o nome do contato: ")

            if procurar_contato in numeros:
                print(f"Telefone: {numeros[procurar_contato]}")
            else:
                print("Telefone não registrado")

        case 3:
            remover = input("Digite o contato que queira remover: ")

            if remover in numeros:
                del numeros[remover]

        case 4:
            print("Encerrando...")
            break

