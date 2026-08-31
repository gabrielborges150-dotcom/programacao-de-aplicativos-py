import random

numero_secreto = random.randint(1 , 100)

chutes = 1

while True:
    try:
        chute = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Voce deve digitar um numero inteiro!")
        continue

    if chute == numero_secreto:
        print(f"Voce achou! O numero e {numero_secreto}")
        print(f"Voce precisou de {chutes}")
        break
    elif numero_secreto > chute:
        print("O numero e menor!")
        chutes += 1
    else:
        print("O numero e maior!")
        chutes += 1

