## Este proceso simula un flujo de datos en tiempo real a partir de datos historicos
import time   # libreria para simular timepo
import json   #libreria para ocnvertir datos el JSON
from kafka import KafkaProducer
import csv    #libreria para leer CSV

#configuramos el producto
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
#abrimos el archivo csv
with open('datos.csv', encoding='latin-1', errors='ignore') as file:
    reader = csv.DictReader(file)   #leermos el archivo como diccionario
#recorrremos cada fila del archivo
    for row in reader:
#enviamos la fila al topic
        producer.send('topic_tarea3', row)
#mostramos en consola lo que se envia
        print("Enviado:", row)
#esperamos 1 segundo
        time.sleep(1)
