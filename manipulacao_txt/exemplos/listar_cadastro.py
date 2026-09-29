def listar_cadastro():
    itens_cadastro = []
    with open("txts/cadastro.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(";")

        obj = {
            "nome": nome,
            "idade": idade
        }

        itens_cadastro.append(obj)
    print(f"Itens Cadastrados: {itens_cadastro}")

listar_cadastro()