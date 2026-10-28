#1. Encapsulamento
#Proteger o salario para que ele só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #Privado: dois sublinhados

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.__salario:.2f}")

    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self , porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}.")
            return
        self.__salario = self.salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento.")

ana = Funcionario("Ana", 3000)
ana.apresentar()

ana.dar_aumento(10)
ana.apresentar()

#try/except é um bloco usado em programação para tratar erro
try:
    ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salario diretamente.")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado de fora.")

#2. Herança

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)#super chama o construtor da classe chamada
        self.equipe = equipe#Atributo novo

    def mostrar_equipe(self):
        print(self.nome, "gerencia", self.equipe, "pessoas.")

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

fulano = Gerente("Fulano", 8000, 5)
caio = Estagiario("Caio", 1500, "Análise de Sistemas")

fulano.apresentar()
caio.apresentar()
caio.dar_aumento(5)
caio.apresentar()