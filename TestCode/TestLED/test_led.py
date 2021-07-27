import RPi.GPIO as GPIO
import time
import os

print(GPIO.VERSION)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)

GPIO.output(13, True)
time.sleep(2)
#GPIO.output(13, False)


GPIO.cleanup
