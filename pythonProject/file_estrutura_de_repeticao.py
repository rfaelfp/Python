arquivo = input("Informe o nome do arquivo: ")
palavra = input("Informe uma palavra: ")

arq = open('c:\Tmp\ ' + arquivo, 'r')
arqf = open("c:\Tmp\leste-FIND.txt", "w")
for linha in arq:
    if linha.find(palavra) >= 0:
        arqf.write(linha)

arq.close()
arqf.close()
