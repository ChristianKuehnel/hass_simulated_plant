#!/usr/bin/python3

from datetime import datetime
import json
import random
import time

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', 1883, 60)


while(True):
  send_msg = {
    'battery': random.randrange(80, 100, 1),
    'temperature': random.randrange(0, 30, 1),
    'brightness': random.randrange(40, 100, 1),
    'moisture': random.randrange(10, 70, 1),
    'conductivity': random.randrange(40, 70, 1),
    'timestamp': datetime.now().isoformat(),
  }
  client.publish('test/simulated_plant', payload=json.dumps(send_msg), qos=0, retain=False)
  print(send_msg)
  time.sleep(10)


