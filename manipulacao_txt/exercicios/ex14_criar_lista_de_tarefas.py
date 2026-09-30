import os

ARQUIVO = "txts/tarefas.txt"

def adicionar_tarefas():
    os.makedirs("txts", exist_ok=True)
    texto = input("Digite a nova tarefa: ")
    with open(ARQUIVO, "a", encoding="utf-8") as arq:
        arq.write(f"--> {texto}\n")
        print("Tarefa Adicionada!")

def listar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            print(arq.read())
    else:
        print("Nenhuma tarefa encontrada.")

def remover_tarefa():
    if not os.path.exists(ARQUIVO):
        print("Nenhuma tarefa para remover.")
        return

    with open(ARQUIVO, "r", encoding="utf-8") as arq:
        linhas = arq.readlines()

    listar_tarefas()
    pos = int(input("Digite o número da tarefa a remover (1, 2, ...): ")) - 1

    if 0 <= pos < len(linhas):
        linhas.pop(pos)
        with open(ARQUIVO, "w", encoding="utf-8") as arq:
            arq.writelines(linhas)
        print("Tarefa removida!")
    else:
        print("Posição inválida.")

def gerenciar_tarefas():
    while True:
        print("\n=== Super Lista de Tarefas ===")
        print("1 - Adicionar tarefa | 2 - Listar | 3 - Remover | 0 - Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "0":
            break
        elif opcao == "1":
            adicionar_tarefas()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()


gerenciar_tarefas()