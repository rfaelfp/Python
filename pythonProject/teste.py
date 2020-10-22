from try_parse.utils import ParseUtils

string = input("Digite: ")
string_verif = '0123456789'
contador = 0
numero = False

for elem in string:
    for elem_verif in string_verif:
        if elem == elem_verif:
            contador += 1
            if contador == len(string):
                numero = True

print("É um número" if numero else "Não é um número")

'''
# Exemplo utilizando a biblioteca ParseUtils

from try_parse.utils import ParseUtils

string = input("Digite: ")
status, target = ParseUtils.try_parse_int(string)
print(status, target)
'''

