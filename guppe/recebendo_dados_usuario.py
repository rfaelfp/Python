"""
Recebendo dados do usuário

input() -> Todo dado recebido do tipo input é do tipo String.

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Simples -> 'Angelina Jolie.'
- Duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
...
"""
# Entrada de dados
# print("Qual seu nome? ")
# nome = input()
# Simplificando
nome = input("Qual o seu nome: ")

# Exemplo de print 'antigo' python 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print 'moderno' python 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' python 3.7
print(f'Seja bem vindo(a) {nome}')

# Exemplo de print 'mais atual' python 3.7
# print("Qual sua idade: ")
# idade = input()

idade = int(input("Qual sua idade: "))

# Processamento

# Saída de dados

# Exemplo de print 'antigo' python 2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' python 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' python 3.7
print(f'A {nome} tem {idade} anos')

"""
int(idade) -> Cast
Cast é a 'conversão' de um tipo de dado para outro. 
"""

print(f'A {nome} nasceu em {2020 - idade}')
