def imprimir(limite):
    inicio = 0
    for i in range(limite):
        inicio += 1
        for j in range(inicio):
            print(inicio, end="\t")
            if j == (inicio - 1):
                print("\n")


limite = int((input("Digite o número desejado: ")))
imprimir(limite)
