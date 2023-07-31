import requests

endpoint = "http://localhost:8000/api"
# endpoint = "http://httpbin.org/anything"

get_response = requests.post(endpoint, json={"title": "Hello world",
                                             "content": "Hello world", 
                                             "price": "abc123"})


# HTTP request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object notation ~ Python Dict
# print(get_response.text)
print(get_response.json())
print(get_response.status_code)
