import csv

def exibir_alunos():
    with open("../csv/alunos.csv", "r", encoding="utf-8") as arq:
        alunos = csv.DictReader(arq)

        for aluno in alunos:
            print(aluno)

exibir_alunos()