def ler_arquivo(file):
    with open(F"txts/{file}.txt", "r", encoding="utf-8") as arquivo:
        print("\n" + arquivo.read())

def adicionar_texto(file):
    with open(f"txts/{file}.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(input("Digite o conteúdo a ser adicionado: "))

def sobrescrever_arquivo(file):
    with open(f"txts/{file}.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(input("Digite o texto para sobrescrever: "))


def menu_arquivo():
    while True:
        print("\n===== Menu de Operações com Arquivos TXT =====")
        print("1 - Ler arquivo")
        print("2 - Adicionar texto")
        print("3 - Sobrescrever arquivo")
        print("0 - Sair")

        opcao = input("Digite sua opção: ").strip()

        if opcao == "0":
            print("Saindo do programa...")
            break

        if opcao in ("1", "2", "3"):
            arquivo = input("Digite o nome do arquivo: ").strip()

            if opcao == "1":
                ler_arquivo(arquivo)
            elif opcao == "2":
                adicionar_texto(arquivo)
            elif opcao == "3":
                sobrescrever_arquivo(arquivo)
        else:
            print("Opção inválida! Tente novamente.")


menu_arquivo()