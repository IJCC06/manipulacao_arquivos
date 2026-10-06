import csv

def salvar_alunos():
    alunos = [
        ["Renan", 40, "Python"],
        ["Moisés", 43, "IoT"],
        ["Rafael", 43, "Eletrônica"],
        ["Maristela", 19, "React"],
        ["Katia", 35, "Java"]
    ]

    with open("../csv/alunos.csv", "w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)

        escritor.writerow(["Nome", "Idade", "Curso"])
        escritor.writerows(alunos)

salvar_alunos()