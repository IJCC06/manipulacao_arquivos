import csv

def ler_csv():
    with open("../csv/alunos.csv", "r", encoding="utf-8") as arq:
        l = csv.reader(arq)

        next(l)

        for linha in l:
            print(linha)

ler_csv()