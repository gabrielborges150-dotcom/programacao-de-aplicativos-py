class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    @property
    def ler_nota(self):
        return self.__nota

    def definir_nota(self, valor):
        if valor >= 0 and valor <= 10:
            self.__nota = valor
        else:
            print("Nota inválida!")

    def situacao(self):
        if self.__nota >= 7:
            print("Aprovado.")
        else:
            print("Reprovado.")

aluno1 = Aluno("Marina", 6.5)
print(aluno1.situacao())# Reprovado
aluno1.definir_nota(15)# Nota inválida!
aluno1.definir_nota(8)
print(aluno1.ler_nota)
aluno1.situacao()

aluno2 = Aluno("Gustavo", 9.0)
print(aluno2.situacao())
aluno2.definir_nota(15)
print(aluno2.ler_nota)
aluno2.situacao()
