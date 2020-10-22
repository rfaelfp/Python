frase = input("Digite a palavra ou frase: ")
vogais = "aeiou"
contador_espaco = 0
contador_vogal = 0

for letra in frase:
    if letra == ' ':
        contador_espaco += 1
    if letra in vogais:
        contador_vogal += 1

print(f'A palavra/frase: "{frase}" possui {contador_espaco} espaços em brancos e {contador_vogal} vogal(is).')

