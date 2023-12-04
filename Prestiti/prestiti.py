'''logging,connessione a couchdb e creazione applicazione con flask'''
import logging
import couchdb
from flask import Flask, request, jsonify
#configurazione del logging
logging.basicConfig(level=logging.INFO,
             filename="Prestiti.log",
            filemode="w",
            format="%(asctime)s - %(levelname)s - %(message)s    ")

app = Flask(__name__)
#stringa di connessione per couchdb prestiti (obbligatorio in minuscolo)
couch = couchdb.Server(url='http://admin:giovanni@couchserver:5984/')
db = couch['prestiti']
logging.info("Connessione al DB")
@app.route('/')
def hello():
    '''prova'''
    return jsonify({'message': 'Benvenuto su couchdb!'})
#Prova

@app.route('/get', methods=['GET'])
def get_data():
    '''get'''
    #ciclo per inserire tutti i documenti
    data = list(db.view('_all_docs', include_docs=True))
    #return della lista con tutti i dati
    return jsonify(data)


@app.route('/get/<doc_id>', methods=['GET'])
def get_data_by_id(doc_id):
    '''get id'''
    # Ritorna un documento con un id specifico
    doc = db.get(doc_id)
    if doc is None:
        return jsonify({'error': 'Document not found.'}), 404
    return jsonify(doc)

@app.route('/crea', methods=['POST'])
def create_data():
    '''create'''
    # Crea un nuovo documento
    # Ottieni i dati dalla richiesta nel body
    data = request.get_json()

    # Salva i dati nel database
    doc_id, doc_rev = db.save(data)

    # Restituisci l'ID e la revisione del documento creato
    return jsonify({'id': doc_id, 'rev': doc_rev})


@app.route('/update/<doc_id>', methods=['PUT'])
def update_data(doc_id):
    '''update'''
    # Update di un documento già presente
    #richiesta dei parametri nel body
    data = request.get_json()
    #prende come riferimento l'id autoassegnato
    data['id'] = doc_id

    db.save(data)
    return jsonify({'id': doc_id, 'rev': data['rev']})



@app.route('/delete/<doc_id>', methods=['DELETE'])
def delete_data(doc_id):
    '''delete'''
    # Delete a document
    if doc_id in db:
        doc = db[doc_id]
        db.delete(doc)
        return jsonify({'message': 'Documento eliminato <3<3<3.'})
    return jsonify({'error': 'Document not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

logging.warning("Run dell'applicazione Prestiti.py")
