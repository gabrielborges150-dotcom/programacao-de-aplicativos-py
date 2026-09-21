def analisar_turma(dicionario_alunos, nota_corte):
    dicionario_aprovados = {}
    dicionario_reprovados = {}

    for nomes, notas in dicionario_alunos.items():

        if notas >= nota_corte:
            dicionario_aprovados[nomes] = notas
        else:
            dicionario_reprovados[nomes] = notas

    media = sum(dicionario_aprovados.values()) / len(dicionario_alunos)

    return media, dicionario_aprovados , dicionario_reprovados

dicionario = {}

try:

    qtd = int(input("Quantas notas vai digitar: "))

    for i in range(qtd):
        nome = str(input(f"Digite o nome do aluno {i + 1}: "))

        nota = float(input(f"Digite a nota do aluno {i + 1}: "))

        dicionario[nome] = nota
    if len(dicionario) > 0:
        media_geral, aprovados , reprovados = analisar_turma(dicionario , 7.0)

        print(f"===Tabela Aprovados===\nAprovados: {aprovados}\nReprovados: {reprovados}\nMedia: {media_geral}")

except ValueError:

    print("Digite apenas numeros.")