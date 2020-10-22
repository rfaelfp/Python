def converter_para_mb(kb):
    valor_conversao = 1_048_576
    kb /= valor_conversao
    return kb


def espaco_total(arq1):
    integral = 0
    for line in arq1:
        integral += int(line[16:28])
    return integral


diretorio = input("Digite o diretório que o arquivo está salvo: ")
arquivo = "usuários.txt"
final = "relatório.txt"
qtd_usuario = 0

arq = open(diretorio + arquivo, 'r')
total = converter_para_mb(espaco_total(arq))
arq.close()

arqf = open(diretorio + final, 'w')
arq = open(diretorio + arquivo, 'r')

arqf.write("ACME inc.\t\t\tUso do espaço em disco pelos usuários\n")
arqf.write("------------------------------------------------------------------------\n")
arqf.write("Nr.\tUsuário\t\t\t\tEspaço utilizado\t% do uso\n")

for linha in arq:
    nome = linha[0:15]
    mbyte = converter_para_mb(float(linha[16:-1]))
    valor_de_uso = 100 * mbyte / total
    qtd_usuario += 1
    arqf.write(f"{qtd_usuario}\t{nome}\t\t\t{round(mbyte, 2)} MB\t\t{round(valor_de_uso, 2)} %\n")

arqf.write(f"\nEspaço total ocupado: {round(total, 2)} MB\n")
arqf.write(f"Espaço médio ocupado: {round((total / qtd_usuario), 2)} MB")

arq.close()
arqf.close()
