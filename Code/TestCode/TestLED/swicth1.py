import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.IN)

while 1:
	print ("sw status ==> " + str(GPIO.input(14)))
	time.sleep(0.2)
