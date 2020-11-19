import requests
import random
import time

write_channel_feed = 'https://api.thingspeak.com/update?api_key=2Q4BUWG1ZVYGVBXK&field'


def get_temp_umid():
    field_temp = "1="
    field_umid = "&field2="
    valor_temp = str(random.randrange(0, 40))
    valor_umid = str(random.randrange(0, 100))
    r = requests.get(write_channel_feed + field_temp + valor_temp + field_umid + valor_umid)
    if r.status_code == 200:
        print(f"{elem + 1}ª inclusão realizada - Temperatura: {valor_temp}º || Umidade: {valor_umid}%")
    else:
        print("Ocorreu um erro!")


for elem in range(15):
    get_temp_umid()
    time.sleep(10)
