import csv

def criar_csv():
    with open("../csv/alunos.csv", "w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)

        escritor.writerow(["Nome", "Idade", "Curso"])
        escritor.writerow(["Renan", 40, "Python"])
        escritor.writerow(["Moisés", 43, "IoT"])
        escritor.writerow(["Rafael", 43, "Eletrônica"])

criar_csv()