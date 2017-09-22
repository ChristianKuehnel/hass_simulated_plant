#!/usr/bin/python3

from datetime import datetime
import json
import random
import time

import paho.mqtt.client as mqtt

while(True):
  try:
    client = mqtt.Client()
    client.connect('localhost', 1883, 60)
  
    send_msg = {
      'battery': random.randrange(1, 100, 1),
      'temperature': random.randrange(0, 30, 1),
      'brightness': random.randrange(0, 5000, 1),
      'moisture': random.randrange(0, 100, 1),
      'conductivity': random.randrange(0, 5000, 1),
      'timestamp': datetime.now().isoformat(),
      }
    client.publish('test/simulated_plant', payload=json.dumps(send_msg), qos=0, retain=False)
    client.disconnect()
    print(send_msg)
  except ConnectionRefusedError:
    print('not connected')

  time.sleep(10)

