'''
Loop for

Loop -> estrutura de repetição
For -> uma dessas estruturas

Utilizamos loops para interar sobre sequencias ou sobre valores iteráveis

Exemplos de iteraveis:
    - String
    - Lista
        lista = [1, 3, 5, 7, 9]
    - Range
        numeros = range(1, 10)

'''

nome = 'Geek Universiy'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1 (iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 2 (iterando sobre um range)
'''
range(valor_inicial, valor_final)
obs.: O valor final não é inclusive
'''
for numero in range(1, 10):
    print(numero)
