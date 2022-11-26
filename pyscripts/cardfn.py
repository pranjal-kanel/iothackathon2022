#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

module=SimpleMFRC522()

def readCard():
    try:
        id, text = module.read()
        GPIO.cleanup()
    except:
        return ""
    finally:
        return text

def writeCard(data):
    try:
        module.write(data)
    except:
        return 0
    finally:
        return 1