import requests
endpoint= "http://127.0.0.1:8000/personne/list/"
response=requests.get(endpoint)
print(response.json())
print(response.status_code)

# HTTP REQUEST ---> HTML
# REST API HTTP  ---> JSON JAVASCRIPT OBJECT NOTATION