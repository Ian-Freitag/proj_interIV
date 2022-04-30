import requests

response = requests.get('https://www.webmotors.com.br/carros-usados/estoque?lkid=1000')

print(response.status_code)