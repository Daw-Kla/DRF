import requests


endpoint = 'http://localhost:8000/api/products/16568516651656516/'

get_response = requests.get(endpoint, verify=False)
print(get_response.json())