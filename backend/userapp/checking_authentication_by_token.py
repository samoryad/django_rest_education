import requests

# проверка на авторизацию через токен
response = requests.post(
    'http://127.0.0.1:8000/api-token-auth/',
    data={
        'username': 'django1',
        'password': 'Zaq11qaz'})

# {'token': '33dd9e2d633aa75d6b53b6a47346a404ed165693'}
print(response.status_code)
print(response.json())  # {'token': '33dd9e2d633aa75d6b53b6a47346a404ed165693'}


# проверка AcceptHeaderVersioning
response = requests.get('http://127.0.0.1:8000/api/users/')
print(response.json())

response = requests.get(
    'http://127.0.0.1:8000/api/users/',
    headers={
        'Accept': 'application/json; version=V2'})
print(response.json())
