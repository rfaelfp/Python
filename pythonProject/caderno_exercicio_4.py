import sqlite3

conn = sqlite3.connect('C:\\Users\\rafael.pedrosa\\Documents\\sistemas_distribuidos\\bdpessoas.db')

cursor = conn.cursor()
verif = True
while verif:
    cursor.execute("SELECT nome, idade FROM PESSOAS")
    for elem in cursor.fetchall():
        print(f"Nome: {elem[0]} - Idade: {elem[2]}")

    resp = input("Deseja cadastrar novo usuário? (s/n): ")
    if resp.lower() == 's':
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        cursor = conn.cursor()
        cursor.execute("insert into pessoas (nome, idade) values('" + nome + "', '" + idade + "')")
        conn.commit()
    else:
        conn.close()
        verif = False
