def carregar_nomes():
    with open("txts/alunos.txt", "r", encoding="utf-8") as arquivo:
        lista_alunos = []
        for nome in arquivo:
            lista_alunos.append(nome.strip())
        print(f"Lista de Alunos:\n{lista_alunos}")

carregar_nomes()