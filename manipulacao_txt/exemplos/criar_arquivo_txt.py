# Modo 'r' - Abre o arquivo para leitura
# Modo 'w' - Abre para escrita e apaga o conteúdo existente
# Modo 'a' - Adiciona novo conteúdo no final do arquivo
# Modo 'x' - Cria um arquivo novo e gera erro se ele já existir


def criar_arquivo():
    # O 'with' fecha o arquivo automaticamente
    # O 'open()' é a função para leitura ou escrita
    with open("txts/alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Lucas\n")
        arquivo.write("Márcio\n")
        arquivo.write("Fábio\n")

criar_arquivo()