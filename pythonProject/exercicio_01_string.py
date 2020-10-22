texto2 = input("Digite a primeira frase: ")
texto1 = input("Digite a segunda frase: ")

print(f"String 1: {texto1}")
print(f"Sring 2: {texto2}")

print(f'Tamanho de "{texto1}": {len(texto1)} caracteres.')
print(f'Tamanho de "{texto2}": {len(texto2)} caracteres.')

tamanho_string = len(texto1) == len(texto2) and "iguais." or "diferentes."
conteudo_string = texto1 == texto2 and "iguais." or "diferentes."

print(f"As duas strings são de tamanhos {tamanho_string}")
print(f"As duas strings possuem conteúdo {conteudo_string}")


