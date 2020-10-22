import serial
import time
import re
import sqlite3

conn = sqlite3.connect('C:\\Users\\rafael.pedrosa\\Documents\\Arduino\\dbTemperatura.db')

cursor = conn.cursor()

comport = serial.Serial('COM5', 9600)
print("Realizado conexão com a porta serial COM5!")


while True:
    temperatura = str(comport.readline())
    temperatura = re.findall(r'\d+', temperatura)
    temperatura = temperatura[0]
    sql = f"INSERT INTO TemperaturaDados (temperatura, data) values({str(temperatura)},datetime())"
    cursor.execute(sql)
    conn.commit()
    print(f"Realizado a inclusão da temperatura de {temperatura}º no banco de dados!")
    time.sleep(60)
