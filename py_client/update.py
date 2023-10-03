import requests

product_id = input('Which product id update?')
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid id')

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/update/'

    data = {
        'title': 'Hello world 1',
        'price': 1.00
    }

    get_response = requests.put(endpoint, json=data, verify=False)
    print(get_response.json())