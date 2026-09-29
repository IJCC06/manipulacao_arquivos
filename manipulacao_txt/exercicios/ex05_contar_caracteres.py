def contar_caracteres():
    with open("txts/mensagem.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(f"Esse arquivo tem {len(conteudo)} caracteres")

contar_caracteres()