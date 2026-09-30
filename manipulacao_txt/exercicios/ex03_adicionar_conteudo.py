def adicionar_frases(file):
    with open(f"txts/{file}.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(input("Digite uma frase: ") +"\n")

adicionar_frases("frase")