import requests
endpoint= "http://127.0.0.1:8000/personne/2/"
response=requests.get(endpoint, json={'name':'anta','age':'34'})
print(response.json())
print(response.status_code)

# HTTP REQUEST ---> HTML