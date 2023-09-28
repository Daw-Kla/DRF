import requests

product_id = input('Which product id update?')
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid id')

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/update/'

    data = {
        'title': 'New title by update',
        'price': 123.00
    }

    get_response = requests.put(endpoint, json=data, verify=False)
    print(get_response.json())