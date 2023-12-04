
#presa un immagine di mysql e impostata la workdir viene copiato lo script SQL dentro /docker-entrypoint-initdb.d/
#Nella stessa directory ci sono anche degli esempi che si possono inserire con curl direttamente
# -curl -d @data.json -H "Content-Type: application/json" -X POST http://localhost:4999/crea
FROM mysql:latest


WORKDIR /db

COPY ./FilldataLibri.sql /docker-entrypoint-initdb.d/

