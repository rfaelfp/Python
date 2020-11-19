import sqlite3
import requests

conn = sqlite3.connect('C:\\Users\\rafael.pedrosa\\Documents\\sistemas_distribuidos\\dbexercicio13.db')
write_channel_feed = 'https://api.thingspeak.com/update?api_key=2Q4BUWG1ZVYGVBXK&field'

valor_temp = input("Digite a temperatura: ")
valor_umid = input("Digite a umidade: ")

field_temp = "1="
field_umid = "&field2="
r = requests.get(write_channel_feed + field_temp + valor_temp + field_umid + valor_umid)
if r.status_code == 200:
    print(f"inclusão realizada - Temperatura: {valor_temp}º || Umidade: {valor_umid}% no ThingSpeak")
else:
    print("Ocorreu um erro!")

cursor = conn.cursor()
sql = f"INSERT INTO Sensores (temperatura, umidade) values({valor_temp}, {valor_umid})"
cursor.execute(sql)
conn.commit()
print(f"Realizado a inclusão da temperatura de {valor_temp}º e umidade {valor_umid}% no banco de dados!")
