#Oque é uma função:

#Uma função é um bloco de código criado para realizar
#uma determinada tarefa

#Ela permite organizar e reutilizar código

#1. Criando uma função

#Utilizar a palavra def para uma função

def saudacao():
    print("Ola, seja bem vindo")

#para executar a função, chamamos seu nome
saudacao()

#2. Função com parâmetro

def saudacao(nome):
    print(f"Ola, {nome}")


saudacao("Ana")

#3. Mais de um parâmetro
def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria" , 17)

#4. Função com cálculo
def somar(num1, num2):
    resultado_soma = num1 + num2
    print(f"Resultado: {resultado_soma}")

somar(1 , 9999)

#5. Retornando um valor
#O return devolve um valor para o local onde a função foi chamada

def somar(num1 , num2):
    return num1 + num2

resultado = somar(10 , 20)
print(resultado)

#6. Função com condição
def verificarIdade(idade):
    if idade > 18:
        return "Maior de idade"
    else: return "Menor de idade"

resultado = verificarIdade(19)
print(resultado)

#7. Parâmetro com valor padrão
#Podemos definir um valor padrão para um parâmetro

def saudacao(nome = "Aluno"):
    print(f"ola , {nome}")

saudacao()
saudacao("joão")

#8. Vários parâmetros
def calcularMedia(nota1 , nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print(calcularMedia(8, 7, 9))

#9. Funções para organizar um programa
def cadastraProduto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    return nome , preco

def exibirProduto(nome , preco):
    print("\n === Produto ===")
    print(f"nome: {nome}")
    print(f"preço: R${preco}")

nome , preco = cadastraProduto()
exibirProduto(nome,preco)