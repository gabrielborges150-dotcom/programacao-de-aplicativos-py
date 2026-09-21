def funcao(a , b , c):
    delta = (b * b) - 4 * a * c



try:
    a = float(input("Digite um numero: "))
    b = float(input("Digite o segundo: "))
    c = float(input("Digite o terceiro "))
except ValueError:
    print("Digite apenas numeros")

x1 , x2 = funcao(a, b, c)