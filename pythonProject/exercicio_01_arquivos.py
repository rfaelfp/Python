diretorio = input("Digite o diretório que o arquivo está salvo: ")
arquivo = input("Digite o nome do arquivo: ")

arq = open(diretorio + arquivo, "r")
validos = []
invalidos = []


for linha in arq:
    controle = 0
    ip = linha.split('.')
    for i in ip:
        i = int(i)
        if i in range(0, 255):
            controle += 1
            if controle == 4:
                validos.append(linha)
        else:
            invalidos.append(linha)
            break

arq.close()

arqf = open(diretorio + "arquivo_saida.txt", "w")
arqf.write("[Endereços válidos:]\n")
for i in validos:
    arqf.write(i)

arqf.write("\n[Endereços inválidos:]\n")
for j in invalidos:
    arqf.write(j)

arqf.close()
