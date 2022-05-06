import requests

response = requests.get('https://www.kavak.com/br/ordem-menor-preco/carros-usados')

print(response.status_code)