import requests

endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(
    endpoint, json={"title": "New product", "price": 32.99})
print(get_response.json())
