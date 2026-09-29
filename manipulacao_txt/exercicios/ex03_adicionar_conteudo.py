def adicionar_frases():
    with open("txts/frase.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(input("Digite uma frase: ") +"\n")

adicionar_frases()