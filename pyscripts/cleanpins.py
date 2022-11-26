#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.cleanup()
subprocess.run(['echo','PinsCleaned'])