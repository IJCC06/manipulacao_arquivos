import csv

ARQUIVO_T = "../csv/treinadores.csv"
ARQUIVO_P = "../csv/pokemons.csv"

def buscar_treinador(nome):
    """Devolve a linha do treinador ou None se não existir."""
    nome = nome.strip().lower()
    with open(ARQUIVO_T, "r", newline="", encoding="utf-8") as arq:
        for linha in csv.DictReader(arq):
            if linha["nome"].strip().lower() == nome:
                return linha
    return None

def listar_pokemons_treinador():
    nome = input("Digite o nome do treinador que deseja buscar: ").strip()

    treinador = buscar_treinador(nome)
    if treinador is None:
        print("Treinador não encontrado")
        return None

    pokemons = []
    with open(ARQUIVO_P, "r", newline="", encoding="utf-8") as arq:
        for linha in csv.DictReader(arq):
            if linha["treinador"].strip().lower() == treinador["nome"].strip().lower():
                pokemons.append(linha)

    if not pokemons:
        print(f"{treinador['nome']} não possui Pokémon cadastrados.")
    else:
        print(f"{treinador['nome']} possui {len(pokemons)} Pokémon:")
        for p in pokemons:
            print(f"- {p['nome']}")
    return pokemons

def contar_pokemons():
    nome = input("Digite o nome do treinador: ").strip()

    treinador = buscar_treinador(nome)
    if treinador is None:
        print("Treinador não encontrado")
        return None

    total = 0
    with open(ARQUIVO_P, "r", newline="", encoding="utf-8") as arq:
        for linha in csv.DictReader(arq):
            if linha["treinador"].strip().lower() == treinador["nome"].strip().lower():
                total += 1

    print(f"{treinador['nome']} possui {total} Pokémon.\n")
    return total

def pokemon_maior_nivel():
    nome = input("Digite o nome do treinador: ")

    treinador = buscar_treinador(nome)
    if treinador is None:
        print("Treinador não encontrado!")
        return None

    maior_nivel = None
    maior_pokemon = None
    with open(ARQUIVO_P, "r", newline="", encoding="utf-8") as arq:
        for linha in csv.DictReader(arq):
            if linha["treinador"].strip().lower() == treinador["nome"].strip().lower():
                nivel = int(linha["nivel"])
                if maior_nivel is None or nivel > maior_nivel:
                    maior_nivel = nivel
                    maior_pokemon = linha
    print(f"O Pokémon de maior nível de {treinador["nome"]} é {maior_pokemon["nome"]}, de nível {maior_nivel}")

def pokemon_menor_nivel():
    nome = input("Digite o nome do treinador: ")

    treinador = buscar_treinador(nome)
    if treinador is None:
        print("Treinador não encontrado!")
        return None
    


def menu():
    while True:
        print("===== POKÉMON DOS TREINADORES =====")
        print("1 - Listar Pokémon de um treinador")
        print("2 - Contar Pokémon de um treinador")
        print("3 - Mostrar Pokémon de maior nível")
        print("4 - Mostrar Pokémon de menor nível")
        print("5 - Listar Pokémon de determinado tipo")
        print("0 - Voltar ao menu")

        opcao = input("Digite sua opção: ")

        if opcao == "0":
            break
        if opcao == "1":
            listar_pokemons_treinador()
        if opcao == "2":
            contar_pokemons()
        if opcao == "3":
            pokemon_maior_nivel()

menu()