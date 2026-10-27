class Cofre:

    def __init__(self, senha):
        self.__senha = senha
        self.__itens = []
        self.__aberto = False
        self.__tentativas = 0
        self.__bloqueado = False
    
    def abrir(self, senha):
        if self.__bloqueado != True:
            if senha == self.__senha:
                self.__tentativas = 0
                self.__aberto = True  
                print("\nSenha correta! O cofre foi aberto")
            else:
                self.__tentativas += 1
                print(f"\nSenha incorreta! Tentativa {self.__tentativas} de 3")

                if self.__tentativas == 3:
                    self.__bloqueado = True
                    print("\nCofre bloqueado!")
    
    def fechar(self):
            self.__aberto = False
            print("Cofre fechado!")
            return self.__aberto 

    def guardar(self, item):
        if self.__aberto == True:
            if item == " ":
                print("Nada para adicionar.")
            else:
                self.__itens.append(item)
                print(f"Item {item} adicionado ao cofre.")
        else:
            print("Abra o cofre primeiro")
    
    def ver_itens(self):
        if len(self.__itens) > 0:
            print(self.__itens)
        else:
            print("Não há itens")


cofre = Cofre("1234")
cofre.guardar("Relógio")  # Abra o cofre primeiro!
cofre.abrir("0000")  # Senha incorreta! Tentativa 1 de 3.
cofre.abrir("1234")  # Cofre aberto.
cofre.guardar("Relógio")  # Relógio guardado.
cofre.ver_itens()  # Itens: ['Relógio']
cofre.fechar()  # Cofre fechado.

cofre.abrir("1")  # Senha incorreta! Tentativa 1 de 3.
cofre.abrir("2")  # Senha incorreta! Tentativa 2 de 3.
cofre.abrir("3")  # Senha incorreta! Tentativa 3 de 3.

cofre.abrir("1234")  # Cofre bloqueado!