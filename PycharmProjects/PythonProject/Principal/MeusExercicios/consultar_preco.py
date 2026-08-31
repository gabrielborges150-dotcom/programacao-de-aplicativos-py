def consultar_preco(estoque, produto_desejado):
    if produto_desejado in estoque:
        return f"R$ {estoque[produto_desejado]:.2f}"
    return "Produto não encontrado."


dicionario = {}

while True:
    try:
        escolha = int(
            input("\n[1] Adicionar item\n[2] Buscar item\n[3] Sair\nR: ")
        )

        match escolha:
            case 1:
                qtd = int(input("Quantos itens vai adicionar: "))
                for i in range(qtd):
                    nome = (
                        input(f"Digite o nome do item {i + 1}: ")
                        .strip()
                        .lower()
                    )
                    preco = float(input(f"Digite o preço de '{nome}': R$ "))

                    dicionario[nome] = preco
                print("Item(ns) cadastrado(s) com sucesso!")

            case 2:
                busca = (
                    input("Digite o nome do produto para buscar: ")
                    .strip()
                    .lower()
                )
                resultado = consultar_preco(dicionario, busca)
                print(f"Resultado: {resultado}")

            case 3:
                print("Saindo do programa...")
                break  # Encerra o while True

            case _:
                print("Opção inválida! Escolha 1, 2 ou 3.")

    except ValueError:
        print("Digite apenas números válidos!")