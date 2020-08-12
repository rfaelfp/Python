"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python
The Zen of Python
A idéia da PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Camel Case para nome de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] -  Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para a identação (NÃO USE TAB)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar: (importar classes de um pacote)

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de
# constantes ou variáveis locais.

- Imports devem ser feitos em linhas separadas

[6] - Espaços em expressões e instruções


# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 5
y              = 3
variavel_longa = 10

# Faça:

x = 5
y = 3
variavel_longa = 10

[7] - Termine sempre uma instrução com uma nova linha
"""
import this
