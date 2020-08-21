'''

Estruturas lógicas: and (e), or (ou), not (não) e is (é)

Operadores unários:
    - not
Operador binários:
    - and, or, is

Para o 'and', ambos os valores precisam ser true.
Para o 'or', um ou outro valor precisa ser true.
Para o 'not', o valor do booleano é invertido, ou seja se for true vira false e vice-versa.
Para o 'is', o valor é comparado com um segundo.

'''

ativo = False
logado = False

if ativo is False:
    print('Você precisa ativar sa conta. Por favor cheque seu e-mail!')
else:
    print('Bem-vindo usuário!')
