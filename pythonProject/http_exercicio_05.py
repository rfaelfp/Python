import requests

r = requests.get('http://www.google.com/search', params={'q': 'rafael ferreira'})

if r.status_code == 200:
    print()
    print('Retorno : ', r.text)
    print()

    arq = open("c:\\tmp\\data.html", "w")
    arq.write(r.text + "\n")
    print("Arquivo alterado foi ", arq.name)

    arq.close()
else:
    print('Nao houve sucesso na requisicao.')
