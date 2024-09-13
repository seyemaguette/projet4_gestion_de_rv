import requests
id = input("Entre l'id que tu veut supprimer\n")
endpoint= f"http://127.0.0.1:8000/personne/delete/{id}/"
response=requests.delete(endpoint)
print(response.status_code,response.status_code==204)
