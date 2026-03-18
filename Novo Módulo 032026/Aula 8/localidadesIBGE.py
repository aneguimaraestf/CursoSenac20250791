# https://servicodados.ibge.gov.br/api/v1/localidades/estados

# Faça uma requisição ao endpoint de estados do IBGE
# A partir do resultado da requisição imprima o nome de todos os estados do Brasil


import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
resposta = requests.get(url)

estados = resposta.json()
print(f"São {len(estados)} estados:")
print()
for estado in sorted(estados, key=lambda x: x["nome"]):
    print(f"{estado['nome']} - {estado['regiao']['nome']}")
