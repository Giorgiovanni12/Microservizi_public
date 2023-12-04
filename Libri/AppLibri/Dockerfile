#Dockerfile di base che prende un immagine di python,viene impostata una directory in cui lavorare,e viene copiato il file
#di testo requirements.txt dove ci sono le varie librerie da importare.Vengono installate con pip e viene copiato il file 
#con dentro l'applicazione

FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY libri.py ./
