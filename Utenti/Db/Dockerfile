
#presa un immagine di mysql e impostata la workdir viene copiato lo script SQL dentro /docker-entrypoint-initdb.d/

FROM mysql:latest


WORKDIR /db

COPY ./Utenti.sql /docker-entrypoint-initdb.d/

