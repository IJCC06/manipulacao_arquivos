def ler_arquivo(file):
    with open(f"txts/{file}.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

ler_arquivo("mensagem")