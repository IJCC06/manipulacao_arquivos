def buscar_nome():
    nome_entrada = input("Digite o nome para pesquisar: ").lower()
    with open("txts/nomes.txt", "r", encoding="utf-8") as arquivo:
        lista_alunos = []
        for nome in arquivo:
            lista_alunos.append(nome.strip().lower())

    if nome_entrada in lista_alunos:
        print("Nome Encontrado!")
    else:
        print("Nome não encontrado!")

buscar_nome()