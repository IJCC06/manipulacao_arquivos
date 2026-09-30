def cadastrar_produtos():
    with open("txts/produtos.txt", "a", encoding="utf-8") as arq:
        produto = {}

        print("Cadastro de Produto:")
        produto["nome"] = input("Digite o nome do produto: ")
        produto["preco"] = float(input("Digite o preco: "))
        produto["quantidade"] = int(input("Digite a quantidade: "))

        for valor in produto:
            arq.write(str(produto[valor]) + ";")
        arq.write("\n")

cadastrar_produtos()