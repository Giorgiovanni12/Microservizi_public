'''import delle librerie time e kafka '''
import time

from confluent_kafka import Consumer
#sleep di qualche secondo
time.sleep(150)
#configurazione kafka
conf = {
    'bootstrap.servers': 'kafka',
    'group.id': '1',
}

consumer = Consumer(conf)

# Subscribe al topic microservizi
consumer.subscribe(['microservizi'])

while True:
    msg = consumer.poll(timeout=1.0)
    #print di tutti i messaggi se c'è il messaggio
    if msg is not None:
        print(f"Consumed event from topic {msg.topic()}, value = {msg.value().decode('utf-8'):12}"
        .format(
        topic=msg.topic(), value=msg.value().decode('utf-8')))
