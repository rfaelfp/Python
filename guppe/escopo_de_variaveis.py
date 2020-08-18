'''
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais
    - São reconhecidas, ou seja, seu escopo compreende todo o programa.
2 - Variáveis locais
    - Sõo reconhecidas somente no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco.

Para declarar variáveis em python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nos não colocamos
o tipo de dado nela. Esse tipo é auferido ao atribuirmos um valor à mesma.

'''

# Exemplo de variável local
numero = 2
print(numero)
print(type(numero))

# Mostrando a tipagem dinâmica
numero = 'Geek'
print(numero)
print(type(numero))

# Variável local
numero = 2
if numero > 10:
    novo = numero + 10  # se não entrar na condição a variável novo nunca irá existir
    print(novo)

print(novo)
