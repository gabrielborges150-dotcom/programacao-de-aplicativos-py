# 1. Classe: o modelo (planta)

class Celular:
    def __init__(self, marca, modelo, cor, bateria=100):
        # Atributos: as características de um objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    # 4. Métodos: comportamentos do objeto
    def ligar(self):
        # O método consulta um atributo do próprio objeto
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar.")
        else:
            self.ligado = True
            print("Ligado")

    def desligar(self):
        self.ligado = False
        print("Desligado")


# 5. Objetos: criados a partir da classe (casa)
celular1 = Celular("Samsung", "Galaxy S23", "preto", 70)
celular2 = Celular("Motorola", "Moto G54", "azul", 0)

# 6. Acessando e alterando atributos - Usamos objeto.atributo
print(celular1.marca)
print(celular1.modelo)

print(celular2.cor)
print(celular2.bateria)

# 7. Chamando métodos - Usamos objeto.metodo()
celular2.ligar()
celular2.desligar()