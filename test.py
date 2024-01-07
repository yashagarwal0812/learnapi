import requests

url = 'http://127.0.0.1:8000/users/me/items/'

headers = {
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aW0iLCJleHAiOjE3MDQ1NzQ3MDV9.ywCYZbNk0oC-RbaD66AyTA95ikPJQcnWb4k-Asty4AE",
}

response = requests.get(
    url,
    headers=headers,
)

print(response.json())  # 👉️ 201
