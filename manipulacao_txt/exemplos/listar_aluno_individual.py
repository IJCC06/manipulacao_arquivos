def listar_aluno_individual():
    lista_alunos = []
    with open("txts/alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista_alunos.append(linha.strip())

    print(f"Lista de Alunos: {lista_alunos}")

listar_aluno_individual()