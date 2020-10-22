import requests

url = 'https://viacep.com.br/ws/MG/Belo Horizonte/'
rua = 'Rua dos Aimores'
formato = '/json/'

r = requests.get(url + rua + formato)

if r.status_code == 200:
    for end in r.json():
        print(end)
else:
    print('Nao houve sucesso na requisicao.')
