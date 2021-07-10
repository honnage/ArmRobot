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

ledStartPin = 12 #Yellow
ledWorkingPin = 13 #Purple
SwicthButtonWork = 11 #Blue
sw = 3

GPIO.setup(ledStartPin, GPIO.OUT)
GPIO.setup(ledWorkingPin, GPIO.OUT)
GPIO.setup(sw , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SwicthButtonWork , GPIO.IN, pull_up_down=GPIO.PUD_UP)


status_ledWorkingPin = False



try:
	GPIO.output(ledStartPin, GPIO.LOW)
	GPIO.output(ledWorkingPin, GPIO.LOW)	
	
	while True:	
		print ("LED Start: ON")
		if status_ledWorkingPin == False:
			while status_ledWorkingPin == False:
				if GPIO.input(SwicthButtonWork):
					print("Port sw is 1/HIGH/True - LED ON")
					GPIO.output(ledStartPin, 1)	
				
				else:
					print("Port sw is 0/LOW/False - LED OFF\n")
					GPIO.output(ledStartPin, 0)
					print ("LED Start: OFF")
					GPIO.output(ledStartPin, GPIO.LOW)
					status_ledWorkingPin = True
					
				time.sleep(0.1)
		
		
		if status_ledWorkingPin == True:
			print ("LED Working: ON")
			while status_ledWorkingPin == True:
				if GPIO.input(SwicthButtonWork):
					
					GPIO.output(ledWorkingPin, GPIO.HIGH)
					print("\nLED Working... ON")
					time.sleep(0.1)
					
					GPIO.output(ledWorkingPin, GPIO.LOW)
					print("LED Working... OFF")
					time.sleep(0.1)
					
				else:
					print("LED Working: OFF")
					status_ledWorkingPin = False
					GPIO.output(ledWorkingPin, GPIO.LOW)
					time.sleep(0.1)
					
		
					
			
		if GPIO.input(sw):
			print("Port sw is 1/HIGH/True - LED ON")	
				
		else:
			print("Port sw is 0/LOW/False - LED OFF\n")

finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
