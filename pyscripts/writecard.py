#!/usr/bin/env python
import sys
import subprocess
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

module=SimpleMFRC522()

def writeCard(data):
    try:
        module.write(data)
        GPIO.cleanup()
    except:
        sys.exit('Could Not Write Data')
    finally:
        outText = 'cardWrite--> '+data
        subprocess.run(['echo',outText])
    
argsList = sys.argv
writeCard(argsList[1])
exit()
