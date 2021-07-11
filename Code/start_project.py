from __future__ import division
from threading import Thread
import multiprocessing as mp
import RPi.GPIO as GPIO
import time
import os

print(GPIO.VERSION)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GreenLED = 12 #Yellow
YelloLED = 13 #Purple

SwicthButtonGreen = 11 #Blue
SwicthButtonRed = 40 #

sw = 3

GPIO.setup(GreenLED, GPIO.OUT)
GPIO.setup(YelloLED, GPIO.OUT)

GPIO.setup(sw , GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(SwicthButtonGreen , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SwicthButtonRed , GPIO.IN, pull_up_down=GPIO.PUD_UP)


isSwicthButtonGreen = False
isSwicthButtonRed = False

def SwicthButtonGreen():
	command = "python Swicth_GreenButton.py"
	os.system(command)
	print("Run file Swicth_GreenButton.py")
	global isSwicthButtonGreen 
	isSwicthButtonGreen = False
	return isSwicthButtonGreen

def SwicthButtonRed():
	command = "python Swicth_RedButton.py"
	os.system(command)
	print("Run file Swicth_RedButton.py")
	global isSwicthButtonRed 
	isSwicthButtonRed = False
	return isSwicthButtonRed



status_GreenLED_Working = False
status_RedLED_Working = False

try:
	GPIO.output(GreenLED, GPIO.LOW)
	GPIO.output(YelloLED, GPIO.LOW)	
	
	while True:
		Thread(target=SwicthButtonGreen).start()
		Thread(target=SwicthButtonRed).start()

		
finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
