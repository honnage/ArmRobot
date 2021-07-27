import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.IN)

while 1:
	print ("sw status ==> " + str(GPIO.input(27)))
	time.sleep(0.2)
