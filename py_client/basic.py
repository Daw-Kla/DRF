import requests


#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

get_response = requests.post(endpoint, params={"abc": 123}, json={"title":"hello world"}, verify=False)  #Aplication programming interface API

#print(get_response.text)

#HTTP Request -> HTML
#REST API HTTP Request -> JSON
#JavaScript Object notation ~ python dict

print(get_response.json())
print(get_response.status_code)