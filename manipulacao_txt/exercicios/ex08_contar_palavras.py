def contar_palavras():
    with open("txts/frase.txt", "r", encoding="utf-8") as arquivo:
        qtde_palavras = len(arquivo.read().split())

    print(f"O total de palavras é {qtde_palavras}")

contar_palavras()