import paho.mqtt.client as mqtt
import json

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    dado = json.loads(message.payload.decode())

    loja = dado['id'].split("-")[0]
    tipo = dado['id'].split("-")[1]
    temperatura = dado['temperatura']

    if (tipo == "f01" or tipo == "f02"):
        if (int(temperatura) > -15 or int(temperatura) < -25):
            print(f"Loja: {loja} - Tipo: {tipo} - Temperatura: {temperatura} - ALERTA!")
        else:
            print(f"Loja: {loja} - Tipo: {tipo} - Temperatura: {temperatura}")
    else:
        if (int(temperatura) > 10 or int(temperatura) < 2):
            print(f"Loja: {loja} - Tipo: {tipo} - Temperatura: {temperatura} - ALERTA!")
        else:
            print(f"Loja: {loja} - Tipo: {tipo} - Temperatura: {temperatura}")

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        # print("Conexão bem sucedida!")
        client.subscribe("test/topic")
    else:
        print(f"Conexão falhou! Código {reason_code}")
        exit(reason_code)

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()