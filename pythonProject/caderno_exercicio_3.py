import sqlite3

nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
sql = "INSERT INTO pessoas VALUES ( "
conn = sqlite3.connect('C:\\Users\\rafael.pedrosa\\Documents\\sistemas_distribuidos\\bdpessoas.db')
cursor = conn.cursor()

cursor.execute()

conn.commit()

conn.close()
