'''import libreria di base python per testare tutte le CRUD'''
import requests

# Test per la get di tutti gli utenti
response = requests.get('http://localhost:5000/get',timeout=30)
print(response.json())  #  JSON format

# Test per la get con id associato
response = requests.get('http://localhost:5000/get/3',timeout=30)
print(response.json())  # JSON format

data = {
    "ID":17,
    "Nome":"Giorgio",
    "Cognome":"Vanni",
    "Mail":"micio.miao",
    "Telefono":1448818
  }

response = requests.post('http://localhost:5000/crea', json=data,timeout=30)
print(response.text)

# Update della risorsa con id 2
dataput = {
    "ID":2,
    "Nome":"LUCIA",
    "Cognome":"BIMBIMBAMABM",
    "Mail":"BUMBUM.miao",
    "Telefono":1448818
  }
response = requests.put('http://localhost:5000/update/2', json=dataput,timeout=30)
print(response.text)  # utente modificato

# Test  DELETE di un utente
response = requests.delete('http://localhost:5000/delete/2',timeout=30)
print(response.text)  # utente cancellato

# Testing delle CRUD per l'app utenti




# Test get di tutti i libri
response = requests.get('http://localhost:4999/get',timeout=30)
print(response.json())  #  JSON format

# Test della get con id 2
response = requests.get('http://localhost:4999/get/2',timeout=30)
print(response.json())  #  JSON format

# Test the '/crea' endpoint
datalibri = {

    "ID":15,
    "Titolo":"Il Piacere",
    "Autore":"Gabriele D Annunio",
    "Editore":"Mondadori",
    "Genere":"Romantico",
    "CopieDisponibili":12
  }
response = requests.post('http://localhost:4999/crea', json=datalibri,timeout=30)
print(response.text)  # Print the response message

# Test the '/update/<id>' endpoint
updatedata2 = {

    "ID":15,
    "Titolo":"Il Piacere",
    "Autore":"Gabriele D Annunio",
    "Editore":"Feltirnelli",
    "Genere":"Romantico",
    "CopieDisponibili":12
  }
response = requests.put('http://localhost:4999/update/15', json=updatedata2,timeout=30)
print(response.text)  # Print utente aggiornato

# Test della delete sul libro con id 16
response = requests.delete('http://localhost:4999/delete/15',timeout=30)
print(response.text)  # Print utente cancellato


#fine dei test sulle CRUD dei libri





# Prova
response = requests.get('http://localhost:4998/',timeout=30)
print(response.json())  # JSON format

# Test the '/get' endpoint
response = requests.get('http://localhost:4998/get',timeout=30)
print(response.json())  # JSON format

# Prova della get con id
DOC_ID = 'fa1afc8dea16490c745252c6cf000136'
response = requests.get(f'http://localhost:4998/get/{DOC_ID}',timeout=30)
print(response.json())  # JSON format

# Test della POST
dataprestito = {
    "DataPrestito": "11/02/2022",
    "DataRestituzione": "27/02/2022",
    "IdLibro": "321",
    "IdMatricola": "11",
    "IdPrestito": "121"
}
response = requests.post('http://localhost:4998/crea', json=dataprestito,timeout=30)
data = response.json()

update = {
    "rev":"697",
    "DataPrestito": "11/02/2022",
    "DataRestituzione": "27/02/2022",
    "IdLibro": "3212",
    "IdMatricola": "121",
    "IdPrestito": "11"
}

# PUT Request
put_url = 'http://localhost:4998/update/2d85b3f0498c601291afd57408002540'
response_put = requests.put(put_url, json=update, timeout=30)
print(response_put.text)  # Print the raw response

# DELETE Request
DELETE = '2d85b3f0498c601291afd57408002540'
delete_url = f'http://localhost:4998/delete/{DELETE}'
response_delete = requests.delete(delete_url, timeout=30)
print(response_delete.text)  # Print the raw response