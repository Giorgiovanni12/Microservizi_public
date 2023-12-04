#immagine base di python e il -u serve per mandare su terminale i risultati

FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python3", "-u" , "consumer.py"]