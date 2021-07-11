from __future__ import division
from threading import Thread
import multiprocessing as mp
import RPi.GPIO as GPIO
import time
import os

print(GPIO.VERSION)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GreenLED = 12 #Yellow
YelloLED = 13 #Purple

SwicthButtonGreen = 11 #Blue
#SwicthButtonRed = 40 #

sw = 3

GPIO.setup(GreenLED, GPIO.OUT)
GPIO.setup(YelloLED, GPIO.OUT)

GPIO.setup(sw , GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(SwicthButtonGreen , GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(SwicthButtonRed , GPIO.IN, pull_up_down=GPIO.PUD_UP)

status_GreenLED_Working = False
#status_RedLED_Working = False

try:
	GPIO.output(GreenLED, GPIO.LOW)
	GPIO.output(YelloLED, GPIO.LOW)	
	
	while True:
		
		if status_GreenLED_Working == False:
			print ("\n====================")
			print ("\nSwicth Green case: 1")
			print ("\nStatus GreenLED Working = False")
			print ("\nGreen LED: ON")
		
			while status_GreenLED_Working == False:	
			
				if GPIO.input(SwicthButtonGreen):
						
					GPIO.output(GreenLED, GPIO.HIGH)
					print("\nGreen LED Working... ON")
					time.sleep(1)
						
					GPIO.output(GreenLED, GPIO.LOW)
					print("Green LED Working... OFF")
					time.sleep(1)
					
			
				else:
					print ("\nStatus GreenLED Working = True")
					status_GreenLED_Working = True
					GPIO.output(GreenLED, GPIO.LOW)
					print("Green LED: OFF")
						
				time.sleep(0.01)
						
		# ==============================================================		
				
		if status_GreenLED_Working == True:	
			print ("\n====================")
			print ("\nSwicth Green case: 2")
			print ("\nStatus GreenLED Working = True")
			print ("\nBlue LED: ON")	
		
			while status_GreenLED_Working == True:

				if GPIO.input(SwicthButtonGreen):
						
					GPIO.output(YelloLED, GPIO.HIGH)
					print("\nBlue LED Working... ON")
					time.sleep(0.1)
						
					GPIO.output(YelloLED, GPIO.LOW)
					print("Blue LED Working... OFF")
					time.sleep(0.1)
					
			
				else:
					print ("\nStatus GreenLED Working = False")
					status_GreenLED_Working = False
					GPIO.output(YelloLED, GPIO.LOW)
					print("Blue LED: OFF")
						
				time.sleep(0.01)

finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
