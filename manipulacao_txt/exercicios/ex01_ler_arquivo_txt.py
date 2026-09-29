def ler_arquivo():
    with open("txts/mensagem.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

ler_arquivo()