def listar_aluno():
    with open("txts/alunos.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f"O conteúdo do arquivo 'alunos' é:\n{conteudo}")

listar_aluno()