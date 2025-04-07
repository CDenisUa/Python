import requests

url = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    "title": "post example",
    "body": "body of post example",
    "userId": 123
}
headers = {
    "Content-Type": "application/json",
    "Custom-Header": "ExampleValue"
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

print(data)