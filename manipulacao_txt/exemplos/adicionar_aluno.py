def adicionar_aluno(nome):
    with open("txts/alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome +"\n")

adicionar_aluno("Neymar")
adicionar_aluno("Pelé")
adicionar_aluno("Maradona")