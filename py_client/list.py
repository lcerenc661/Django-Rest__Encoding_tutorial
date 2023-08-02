import requests
from getpass import getpass


endpoint_auth = "http://localhost:8000/api/auth/"
username = input("What is your username? \n")
password = getpass()

get_response_auth = requests.post(endpoint_auth, json={
    "username": username,
    "password": password})
print("PRINTING RESPONSE")
print(get_response_auth.json())

if get_response_auth.status_code == 200:
    token = get_response_auth.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)

    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print(results)
    print(next_url)
    # if next_url is not None:
    #     get_response = requests.get(endpoint, headers=headers)
