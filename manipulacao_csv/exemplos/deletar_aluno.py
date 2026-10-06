import csv

def deletar_aluno():
    with open("../csv/alunos.csv", "r", newline="", encoding="utf-8") as arq:
        l = csv.DictReader(arq)
        alunos = list(l)

    with open("../csv/alunos.csv", "w", newline="", encoding="utf-8") as arq:
        cabecalho = ["Nome", "Idade", "Curso"]
        e = csv.DictWriter(arq, fieldnames=cabecalho)

        e.writeheader()

        aluno_apagar = input("Digite o nome do aluno que deseja apagar: ")
        for aluno in alunos:
            if aluno["Nome"] != aluno_apagar:
                e.writerow(aluno)

deletar_aluno()