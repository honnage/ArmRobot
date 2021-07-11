import RPi.GPIO as GPIO
import time
import os

print(GPIO.VERSION)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, True)
time.sleep(2)
GPIO.output(12, False)


GPIO.cleanup
