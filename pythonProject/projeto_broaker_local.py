import sqlite3
import time
import requests


def get_temperatura(temp, index):
    url_write_channel = 'https://api.thingspeak.com/update?api_key=2Q4BUWG1ZVYGVBXK&field1=' + str(temp)
    r = requests.get(url_write_channel)
    if r.status_code == 200:
        print(f"Enviado com sucesso!"
              f"Incluído o registro {index} do banco de dados no ThingSpeak. Temperatura: {temp} graus.")
    else:
        print("Ocorreu um erro!")


conn = sqlite3.connect('C:\\Users\\rafael.pedrosa\\Documents\\Arduino\\dbTemperatura.db')
sql = "SELECT temperatura, id FROM TemperaturaDados ORDER BY id DESC LIMIT 1;"
cursor = conn.cursor()


while True:
    cursor.execute(sql)
    for elem in cursor.fetchall():
        temperatura = elem[0]
        id = elem[1]
    get_temperatura(temperatura, id)
    time.sleep(60)
