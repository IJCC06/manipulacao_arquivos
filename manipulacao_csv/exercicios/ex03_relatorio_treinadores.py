import csv
from manipulacao_csv.exercicios.ex02_consulta_pokemon_treinador import ARQUIVO_P, ARQUIVO_T

def relatorio_treinador():
    treinador = input("Digite o nome do treinador: ")

    with open(ARQUIVO_T, "r", newline="", encoding="utf-8") as arq:
        for linha in csv.DictReader(arq):
            if linha["nome"] == treinador:
                


def menu():
    while True:
        print("\n===== RELATÓRIOS =====\n")
        print("1 - Relatório de um treinador")
        print("2 - Média de nível dos Pokémon de um treinador")
        print("3 - Média de nível dos Pokémon por tipo")
        print("4 - Quantidade de Pokémon por treinador")
        print("5 - Quantidade de Pokémon por tipo")
        print("6 - Treinadores com nível acima de um valor")
        print("0 - Sair")

        opcao = input("Digite a opção escolhida: ")

        if opcao == "0":
            return None
        elif opcao == "1":