import requests

endpoint = 'http://localhost:8000/api/products/1/'

get_response = requests.get(endpoint, verify=False)  #Aplication programming interface API
print(get_response.json())