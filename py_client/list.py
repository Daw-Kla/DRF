import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'
username = input('What is your username?\n')
password = getpass('What is your password\n')

auth_response = requests.post(auth_endpoint, json={'username': 'admin', 'password': password}) 
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headres = {
        'Authorization': f'Bearer {token}'
    }
    
    endpoint = 'http://localhost:8000/api/products/'

    #listing all objects from DB
    get_response = requests.get(endpoint, headers=headres) 
    print(get_response.json())