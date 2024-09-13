import requests
endpoint= "http://127.0.0.1:8000/personne/update/5/"
response=requests.put(endpoint, json={'name':'nana','age':'34'})
print(response.json())
print(response.status_code)
