import csv

ENDERECO_ARQUIVO = "../csv/treinadores.csv"

def listar_todos_os_treinadores():
    with open(ENDERECO_ARQUIVO, "r", encoding="utf-8") as arq:
        treinadores = csv.DictReader(arq)

        for t in treinadores:
            print(t)


def buscar_treinador_pelo_nome():
    nome = input("Digite o nome que deseja buscar: ")

    with open(ENDERECO_ARQUIVO, "r", newline="", encoding="utf-8") as arq:
        l = csv.DictReader(arq)
        for linha in l:
            if linha["nome"].strip().lower() == nome.strip().lower():
                return linha
    return None


def listar_treinadores_regiao():
    regiao = input("Digite a região que você deseja listar: ").strip().lower()

    with open(ENDERECO_ARQUIVO, "r", newline="", encoding="utf-8") as arq:
        l = csv.DictReader(arq)
        for linha in l:
            if linha["regiao"].strip().lower() == regiao:
                print(linha)
    return None


def treinador_maior_nivel():
    maior_nivel = -1
    maior_linha = None
    with open(ENDERECO_ARQUIVO, "r", newline="", encoding="utf-8") as arq:
        l = csv.DictReader(arq)
        for linha in l:
            nivel = int(linha["nivel"])
            if nivel > maior_nivel:
                maior_nivel = nivel
                maior_linha = linha
    print(f"O treinador com o maior nível é {maior_linha}")


def treinador_menor_nivel():
    menor_nivel = None
    menor_linha = None
    with open(ENDERECO_ARQUIVO, "r", newline="", encoding="utf-8") as arq:
        for linha in csv.DictReader(arq):
            nivel = int(linha["nivel"])
            if menor_nivel is None or nivel < menor_nivel:
                menor_nivel = nivel
                menor_linha = linha
    print(f"O treinador com o menor nível é {menor_linha}")


def main():
    while True:
        print("==== TREINADORES POKÉMON ====")
        print("1 - Listar todos os treinadores")
        print("2 - Buscar treinador pelo nome")
        print("3 - Listar treinadores de uma região")
        print("4 - Mostrar treinador com maior nível")
        print("5 - Mostrar treinador com menor nível")
        print("0 - Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "0":
            break
        if opcao == "1":
            listar_todos_os_treinadores()
        if opcao == "2":
            print(buscar_treinador_pelo_nome())
        if opcao == "3":
            listar_treinadores_regiao()
        if opcao == "4":
            treinador_maior_nivel()
        if opcao == "5":
            treinador_menor_nivel()


main()