def classificar_alunos():
    try:
        with open("txts/alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    nome, nota_str = linha.split(";")
                    nota = float(nota_str)

                    if nota >= 6:
                        print(f"{nome} - {nota} - Aprovado")
                    elif 4 <= nota <= 6:
                        print(f"{nome} - {nota} - Recuperação")
                    elif nota < 4:
                        print(f"{nome} - {nota} - Reprovado")
    except FileNotFoundError, FileExistsError:
        print("Erro: O arquivo 'alunos.txt' não foi encontrado.")

classificar_alunos()