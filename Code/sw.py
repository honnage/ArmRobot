from __future__ import division
from threading import Thread
import multiprocessing as mp
import RPi.GPIO as GPIO
import time
import os

print(GPIO.VERSION)
GPIO.setmode(GPIO.BCM)

ledPin = 18
swPin = 17

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		if GPIO.input(swPin):
			print("Port sw is 1/HIGH/True - LED ON")
			GPIO.output(ledPin, 1)

		else:
			print("Port sw is 0/LOW/False - LED OFF")
			GPIO.output(ledPin, 0)
			
		time.sleep(0.1)

finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
