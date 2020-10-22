def print_data(date):
    date = date.replace("/", "")
    dia = int(date[0:1])
    mes = int(date[2:4])
    ano = int(date[4:9])
    meses = ["janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    print(dia, "de", meses[mes - 1], "de", ano)


data = input("Digite a data: ")
print_data(data)
