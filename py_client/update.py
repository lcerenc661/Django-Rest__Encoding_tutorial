import requests

endpoint = "http://localhost:8000/api/products/6/update/"

data = {'title': 'This is the new title',
        'content': 'This is the content updated'}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)
