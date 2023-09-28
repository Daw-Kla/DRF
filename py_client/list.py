import requests

endpoint = 'http://localhost:8000/api/products/'

#listing all objects from DB
get_response = requests.get(endpoint, verify=False) 
print(get_response.json())