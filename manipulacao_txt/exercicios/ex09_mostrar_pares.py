def mostrar_pares():
    lista_num = []
    with open("txts/numeros.txt", "r", encoding="utf-8") as arquivo:
        for num in arquivo:
            lista_num.append(int(num.strip()))

    lista_num_pares = []
    for item in lista_num:
        if item % 2 == 0:
            lista_num_pares.append(item)
    print(f"Números Pares: {lista_num_pares}")

mostrar_pares()