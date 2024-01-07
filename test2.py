import requests

url = 'http://127.0.0.1:8000/token'

headers = {
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aW0iLCJleHAiOjE3MDQ1NzUyMjZ9.f5QaIjbaHy8IL8hWRUlBcniMy_PgSkv_sQVPB30jqDw",
}

data = {'username': 'tim', 'password': 'tim1234'}

# Send POST request with FORM data using the data parameter
response = requests.post(url, data=data)

# Print the response
print(response.text)
