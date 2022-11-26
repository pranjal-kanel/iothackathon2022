#!/usr/bin/env python
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import subprocess

module=SimpleMFRC522()

def readCard():
    try:
        id, text = module.read()
        GPIO.cleanup()
    except:
        sys.exit("Failed Card Read")
    finally:
        outText = 'cardRead--> '+text
        subprocess.run(['echo',outText])
        
readCard()
exit()