def separar_numeros():
    with open("txts/numeros.txt", "r", encoding="utf-8") as arquivo:
        impar = []
        par = []
        lista_num = []

        for item in arquivo:
            lista_num.append(int(item.strip()))

        for num in lista_num:
            if num % 2 == 0:
                par.append(num)
            else:
                impar.append(num)

        print(f"Números Pares:\n{par}")
        print(f"Números Ímpares:\n{impar}")

separar_numeros()