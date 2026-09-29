def criar_arquivo_txt():
    with open("txts/frase.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(input("Digite uma frase: "))

criar_arquivo_txt()