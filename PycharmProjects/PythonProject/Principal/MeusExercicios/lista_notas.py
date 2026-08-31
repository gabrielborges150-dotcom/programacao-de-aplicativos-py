def analisa_notas(lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    maior_nota = max(lista_notas)

    if media >= 7.0:
        resultado = "Aprovado"
    elif media >= 5.0:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"

    return media, resultado, maior_nota


quantidade_notas = 4
notas = []

for i in range(quantidade_notas):
    while True:
        try:
            nota = float(input(f"Digite a nota {i + 1}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Digite apenas números válidos!")

media_final, situacao, maior = analisa_notas(notas)

print("\n--- Resultado Final ---")
print(f"Média: {round(media_final , 1)}")
print(f"Situação: {situacao}")
print(f"Maior Nota: {maior}")