import serial
import time
import re
import sqlite3

conn = sqlite3.connect('C:\\Users\\rafael.pedrosa\\Documents\\Arduino\\dbTemperatura.db')

cursor = conn.cursor()

comport = serial.Serial('COM5', 9600)
print("Realizado conexão com a porta serial COM5!")

while comport.isOpen():
    temperatura = str(comport.readline())
    temperatura = re.findall(r'\d+', temperatura)
    temperatura = temperatura[0]
    sql = f"INSERT INTO TemperaturaDados (temperatura, data) values({str(temperatura)},datetime('now', '-3 hour'))"
    try:
        cursor.execute(sql)
        conn.commit()
        print(f"Realizado a inclusão da temperatura de {temperatura}º no banco de dados!")

    except cursor:
        print("Algo deu errado na inserção das informações no banco de dados!")
    try:
        comport.write(b'1')
        print("O bip foi executado.")
    except comport:
        print("Algo deu errado na escrita da porta serial!")
    time.sleep(10)
