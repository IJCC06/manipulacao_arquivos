def buscar_produto():
    with open("txts/produtos.txt", "r", encoding="utf-8") as arq:
        produtos = {}
        for linha in arq:
            produto = linha.split(";")
            for n in produto:
                produtos["nome"] = produto[n]

        print(produtos)

buscar_produto()