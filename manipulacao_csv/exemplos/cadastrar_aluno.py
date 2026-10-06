import csv

def cadastrar_aluno():
    with open("../csv/alunos.csv", "a+", newline="", encoding="utf-8") as arq:
        arq.seek(0,2)
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")

        e = csv.writer(arq)
        e.writerow([nome, idade, curso])

        arq.seek(0)
        l = csv.DictReader(arq)

        for linha in l:
            print(linha)

cadastrar_aluno()