'''serve per logging,trasformare in JSON,creare applicazioni con flask e connettersi a mysql'''
import logging
import json
from flask import Flask, request
from flask import jsonify
import sib_api_v3_sdk
from confluent_kafka import Producer
import mysql.connector


app = Flask(__name__)
#Logging configurazione iniziale
logging.basicConfig(level=logging.INFO,
filename="Libri.log",
filemode="w",
format="%(asctime)s - %(levelname)s - %(message)s   ")



# Connection string per mysql al db Libri
conn = mysql.connector.connect(
    user='sa',
    password='Giorgiovanni123!',
    host='dblibri',
    database='Libri')

cursor = conn.cursor()
logging.info("Connessione al DB")

# Configuration per il servizio delle mail
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = (
    'xkeysib-4038bbb8261a4e118ff509c833152d93ff676df070e2b8823951792f53f0a31e-'
    'bzoT9SYcYYiWPKhk'
)
# Creare un istanza per le mail
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Parametri delle mail
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
    to=[sib_api_v3_sdk.SendSmtpEmailTo(email="vannicone0@gmail.com")],
    sender=sib_api_v3_sdk.SendSmtpEmailSender(email="prova@example.com"
    , name="MICROSERVIZI"),
    subject="INSERIMENTO LIBRO",
    html_content="Aggiunto un libro con successo <3."
)

#configurazione kafka
conf = {
    'bootstrap.servers': 'PLAINTEXT://kafka:9092',
    'client.id': 'libri',
    'acks': '1',  
}


producer = Producer(conf)




@app.route('/get', methods=['GET'])
def execute_query():
    '''Get all'''
    cursor.execute('SELECT * FROM Libro')
    results = cursor.fetchall()

    # Converti i risultati in una lista di dizionari
    # Ottieni i nomi delle colonne dal cursore
    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in results]

    # Restituisci i risultati come JSON
    return jsonify(data)

@app.route('/get/<int:idget>', methods=['GET'])
def get_data_by_id(idget):
    '''Get by ID'''
    # Esegui una query per recuperare i dati con l'ID specificato
    cursor.execute('SELECT * FROM Libro WHERE id = %s',(idget,))
    result = cursor.fetchone()

    if result is None:
        return json.dumps({'error': 'Dati non trovati.'}), 404

    colonne = [desc[0] for desc in cursor.description]
    vista = dict(zip(colonne, result))

    # Restituisci i risultati come JSON
    return jsonify(vista)

#Crea un libro
@app.route('/crea', methods=['POST'])
def insert_data():
    '''crea un libro e lo inserisce nel db'''
    #Richiesta dei parametri nella body della POST
    data = request.get_json()

    #I parametri sono bloccati e non si può prescindere da questi
    idlibro = data.get('ID')
    titolo = data.get('Titolo')
    autore = data.get('Autore')
    editore = data.get('Editore')
    genere = data.get('Genere')
    copiedisponibili = data.get('CopieDisponibili')

    #query per inserire il libro all'interno del db,grazie luchino(serviva la f string)
    cursor.execute(f'''INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere,CopieDisponibili)
    VALUES('{idlibro}','{titolo}' , '{autore}', '{editore}', '{genere}','{copiedisponibili}' )''')

    #inserimento dentro il db
    conn.commit()
    topic = "microservizi"
    api_instance.send_transac_email(send_smtp_email)

    key="Creato un utente"

    #crea un messaggio
    value = 'Hai ricevuto una mail <3'
    producer.produce(topic, key=key, value=value)

    return 'Inserito correttamente'




@app.route('/update/<int:idupdate>', methods=['PUT'])
def update_data(idupdate):
    '''update'''
    data = request.get_json()
    #Richiesta dei parametri nella body della POST

    titolo = data.get('Titolo')
    autore = data.get('Autore')
    editore = data.get('Editore')
    genere = data.get('Genere')
    copiedisponibili = data.get('CopieDisponibili')

    # Esegui la query di aggiornamento
    cursor.execute(f"""UPDATE Libro SET Titolo
    = '{titolo}', Autore = '{autore}', Editore = '{editore}', Genere = '{genere}',CopieDisponibili 
    = '{copiedisponibili}' WHERE ID = '{idupdate}'""")

    conn.commit()

    return 'Hai modificato un record daje'

@app.route('/delete/<int:iddelete>', methods=['DELETE'])
def delete_data(iddelete):
    '''delete'''
    # Esegui la query di eliminazione
    cursor.execute(f"DELETE FROM Libro WHERE ID ='{iddelete}'")

    conn.commit()

    return 'Rimosso un Libro dal db <3'

logging.warning("Run dell'applicazione Libri.py")
if __name__ == '__main__':
    app.run(host="0.0.0.0")
# End-of-file (EOF)
