import requests
import random
import time

write_channel_feed = 'https://api.thingspeak.com/update?api_key=2Q4BUWG1ZVYGVBXK&field'


def get_temp():
    field_temp = "1="
    valor_temp = str(random.randrange(0, 40))
    r = requests.get(write_channel_feed + field_temp + valor_temp)
    if r.status_code == 200:
        print(f"{elem + 1}ª inclusão realizada - Temperatura: {valor_temp}º")


def get_umid():
    field_umid = "2="
    valor_umid = str(random.randrange(0, 100))
    q = requests.get(write_channel_feed + field_umid + valor_umid)
    if q.status_code == 200:
        print(f"{elem + 1}ª inclusão realizada - Umidade: {valor_umid}%")


for elem in range(15):
    get_temp()
    time.sleep(10)


for elem in range(15):
    get_umid()
    time.sleep(10)
