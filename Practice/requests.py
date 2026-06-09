import Practice.requests as requests

##GET
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

# print(response)
# print(response.status_code)
# print(response.content)
# print(response.text)
data=response.json()
# print(data)
# print(data["name"])


response =requests.get(
    "https://example.com/users?id=1"
)
# print(response.text)

##POST
payload={
    "name":"Alvish",
    "city":"Ahmedabad"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=payload
)
print(response.status_code)

##PUT
payload = {
    "name": "Updated Name"
}

response = requests.put(
    "https://example.com/users/1",
    json=payload
)

##PATCH
response = requests.patch(
    url,
    json={"name": "New Name"}
)

##With error handling
try:
    response=requests.get(url)
    response.raise_for_status()
    data=response.json()
except requests.exceptions.RequestException as e:
    print(e)   