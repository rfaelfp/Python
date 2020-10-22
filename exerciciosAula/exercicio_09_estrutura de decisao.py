numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

controle = 0

if numero1 > numero2:
    controle = numero1
    numero1 = numero2
    numero2 = controle
if numero2 > numero3:
    controle = numero2
    numero2 = numero3
    numero3 = controle
if numero3 < numero1:
    controle = numero3
    numero3 = numero1
    numero1 = controle
if numero2 < numero1:
    controle = numero1
    numero1 = numero2
    numero2 = controle

print(f"{numero3}, - {numero2}, - {numero1}")
