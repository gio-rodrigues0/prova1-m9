import paho.mqtt.client as mqtt
import time
import json
import csv

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Conecte ao broker
client.connect("localhost", 1891, 60)

def criar_json():
    with open('data.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            dado = {
                "id": row[0],
                "tipo": row[1],
                "temperatura": row[2],
                "timestamp": time.time(),
            }
            publicar(json.dumps(dado))
            time.sleep(1)
    
def publicar(dado):
    message = dado
    client.publish("test/topic", message)

criar_json()

client.disconnect()