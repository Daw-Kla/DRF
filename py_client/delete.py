import requests

product_id = input('Which product id delete?')
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid id')

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/delete/'

    get_response = requests.delete(endpoint, verify=False)  #Aplication programming interface API
    print(get_response.status_code)