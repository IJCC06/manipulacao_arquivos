def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open("txts/cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{idade}")
    print("Aluno Cadastrado com Sucesso!")

cadastrar_aluno()