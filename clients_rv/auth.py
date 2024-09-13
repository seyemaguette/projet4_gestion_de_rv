import requests
from getpass import getpass
endpoint= "http://127.0.0.1:8000/auth/"
username = input('Entrez votre username \n')
password = getpass('Entrez votre password \n')
response=requests.post(endpoint, json={'username':'username','password':'password'})
print(response.json())
print(response.status_code)

# HTTP REQUEST ---> HTML
# REST API HTTP  ---> JSON JAVASCRIPT OBJECT NOTATION