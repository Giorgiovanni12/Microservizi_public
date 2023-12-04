Il progetto ha lo scopo di simulare il funzionamento di una biblioteca.

Mettendo assieme 8 microservizi diversi composti da queste caratteristiche: 

-AppLibri per eseguire operazioni CRUD sul db,viene anche usata come producer di kafka (manda anche una mail quando viene inserito un nuovo libro[usare questo che è gratis https://app.brevo.com/])

-AppUtenti sempre per eseguire operazioni CRUD al proprio db

-AppPrestiti sempre per eseguire operazioni CRUD al proprio db

-DbLibri Db con all'interno tutti i libri

-DbUtenti Db con all'interno tutti gli utenti

-DbPrestiti Db con all'interno tutti i prestiti

-Kafka broker di messaggistica con lo scopo di avvisare l'utente nel momento in cui vengono eseguite alcune operazioni 

-AppConsumer serve per ricevere le notifiche dall AppLibri e stamparle sul terminale

Il progetto nel suo intero prevede:

-CI/CD per pubblicare direttamente su Docker-hub le immagini ogni volta che viene eseguito un push sul repository e controllo del codice manualmente con pylint.

-Logging con lo scopo di monitorare tutte le azioni da parte del container.I log vengono salvati all'interno dei container in un file separato.

-Testing attraverso la libreria request di python che prova ogni singola CRUD .

-Container utilizzo di dokcer e docker-compose per creare tutti i singoli container.Ho provato anche a creare con kompose i file di configurazione ma ho problemi con la vm :(


![Screenshot 2023-11-15 19 59 37](https://github.com/Giorgiovanni12/microservizi/assets/129728209/4703f4f3-1fcb-45da-9dc1-b220c9083850)
