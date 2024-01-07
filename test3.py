import requests

url = 'http://127.0.0.1:8000/token'
url2 = 'http://127.0.0.1:8000/users/me/items/'



data = {'username': 'tim', 'password': 'tim1234'}

# Send POST request with FORM data using the data parameter
response = requests.post(url, data=data)

headers = {
    'Authorization': "Bearer "+response.json()["access_token"],
}

response1 = requests.get(url2, headers=headers)
# Print the response
print(response1.json()[0]['owner']['hashed_password'])

