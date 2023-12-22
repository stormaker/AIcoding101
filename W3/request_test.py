import requests

url = 'http://127.0.0.1:8000/api/create'
data = {"id": 1, "name": "Jack"}

response = requests.post(url, json=data)
print(response.json())
