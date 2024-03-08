import time
import json
import pytest
from prova.pubsub import subscriber

received_message = {'message': 'no message received'}

def on_message_received(topic, payload, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    decoded = payload.decode('utf-8')
    payload = json.loads(decoded)
    global received_message
    received_message = payload