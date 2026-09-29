def contar_linhas():
    with open("txts/alunos.txt", "r", encoding="utf-8") as arquivo:
        qtde_linhas = 0
        for linhas in arquivo:
            qtde_linhas += 1

        print(f"O arquivo possui {qtde_linhas} linhas")

contar_linhas()