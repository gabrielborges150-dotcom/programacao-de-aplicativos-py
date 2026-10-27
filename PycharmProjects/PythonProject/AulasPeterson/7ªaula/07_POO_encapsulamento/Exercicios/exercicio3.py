class Produto:
    def __init__(self, nome, preco, quantidade = 0):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def ler_preco(self):
        return self.__preco

    @property
    def ler_quantidade(self):
        return self.__quantidade

    def entrada(self, quantidade):
        if quantidade <= 0:
            print("Quantidade Inválida!")
        else:
            self.__quantidade += quantidade

    def saida(self, quantidade):
        if self.__quantidade >= quantidade:
            self.__quantidade -= quantidade
            print(f"Saída: de {quantidade}. Estoque: {self.__quantidade}")
        else:
            print(f"Estoque insuficiente! Disponível: {self.__quantidade}")

    def aplicar_desconto(self, porcentagem):
        if porcentagem >= 1 and porcentagem <= 50:
              self.__preco = self.__preco * (1 - (porcentagem / 100))
              print(f"Novo preço: R${self.__preco:.2f}")
        else:
            print("Desconto deve ser entre 1% e 50%!")

    def valor_em_estoque(self):
        return self.__quantidade * self.__preco

fone = Produto("Fone Bluetooth", 150.0, 10)
fone.saida(3)# Saída de 3. Estoque: 7
fone.saida(20)# Estoque insuficiente! Disponível: 7
fone.entrada(-5)# Quantidade inválida!
fone.aplicar_desconto(80)# Desconto deve ser entre 1% e 50%!
fone.aplicar_desconto(10)# Novo preço: R$ 135.00
print(f"R$ {fone.valor_em_estoque():.2f}")

print("\n\n")

celular = Produto("Samsung", 100.0, 10)
celular.saida(4)
celular.saida(20)
celular.entrada(1000)
celular.aplicar_desconto(20)
celular.aplicar_desconto(51)
print(f"R$ {celular.valor_em_estoque():.2f}")
