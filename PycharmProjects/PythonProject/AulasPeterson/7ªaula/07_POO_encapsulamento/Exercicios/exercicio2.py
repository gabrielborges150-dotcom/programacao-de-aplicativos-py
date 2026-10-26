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
        else:
            print("Cofre bloqueado!")
    
    def fechar(self):
            self.__aberto = False
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
