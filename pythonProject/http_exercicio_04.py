import requests

url = 'https://viacep.com.br/abc/'


r = requests.get(url)

if r.status_code == 404:
    print('Erro 404')
    print('A página que você procura não foi encontrada.')
    print()
else:
    print('Nao houve sucesso na requisicao.')
