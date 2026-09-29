def listar_aprovados():
    print("Alunos aprovados:")
    try:
        with open("txts/alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:  # Ignora linhas em branco
                    nome, nota_str = linha.split(";")
                    nota = float(nota_str)

                    if nota >= 6.0:
                        print(f"{nome} - {nota:.1f}")
    except FileNotFoundError:
        print("Erro: O arquivo 'alunos.txt' não foi encontrado.")


# Execução da função
listar_aprovados()