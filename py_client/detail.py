import requests

endpoint = "http://localhost:8000/api/products/3/"

get_response = requests.get(endpoint, json={"title": "Hello world",
                                            "content": "Hello world",
                                            "price": "abc123"})

print(get_response.json())
print(get_response.status_code)
