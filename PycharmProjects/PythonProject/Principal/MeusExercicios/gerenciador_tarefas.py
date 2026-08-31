tarefas = []

contador_adicionar_tarefa = 0
contador_remover_tarefa = 0

while True:

    print("[1] Adicionar Tarefa\n[2] Ver Tarefas\n[3] Remover Tarefa\n[4]FInalizar programa")

    escolha = int(input("R: "))

    match escolha:
        case 1:
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            contador_adicionar_tarefa += 1
        case 2:
            print(tarefas)
        case 3:
            remover = input("Digite a tarefa que queira remover: ")
            tarefas.remove(remover)
            contador_remover_tarefa += 1
        case 4:
            break

print(f"Voce adicionou [{contador_adicionar_tarefa}] tarefas")
print(f"Voce removeu [{contador_remover_tarefa}] tarefas")