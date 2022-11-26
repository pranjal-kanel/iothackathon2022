import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import requests
import time

base_url = 'http://192.168.43.13:8000/attendance'
module=SimpleMFRC522()

while True:
    id, text = module.read()
    payload = {'uniqueid':text}
    print("Payload ==> "+text)
    x = requests.post(base_url,json=payload)
    print(x.text)
    time.sleep(3)
    
    
    