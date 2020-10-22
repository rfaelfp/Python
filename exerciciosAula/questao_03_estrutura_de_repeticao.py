while True:
    nome = str(input("Digite o nome: "))
    if len(nome) > 3:
        break

while True:
    idade = int(input("Digite a idade: "))
    if idade > 0 or idade < 151:
        break

while True:
    salario = float(input("Digite o salário: "))
    if salario > 0:
        break

while True:
    sexo = input("Digite o sexo: ")
    if sexo == 'f' or sexo == 'm':
        break

while True:
    estado_civil = input("Digite o estado civil (s, c, v, d): ")
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
