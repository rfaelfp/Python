"""
Tipo float
Tipo real, decimal
Casas decimais

Obs.: o separador de casas decimais na programação é o ponto e não a vírgula.
"""

# Errado do ponto de vista do float mas gera uma tupla:
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float:
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla artibuição:
valor1, valor2 = 1, 44
print(f'Valor 1: {valor1}')
print(type(valor1))
print(f'Valor 2: {valor2}')
print(type(valor2))

# Podemos converter um float para um int
"""
Ao converter valores float para inteiro nos perdemos precisão.
"""
res = int(valor)
print(f'Resultado: {res}')
print(type(res))

# Podemos trabalhar com números complexos.
variavel = 5j
print(variavel)
print(type(variavel))
