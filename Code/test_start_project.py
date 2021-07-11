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

status_GreenLED_Working = False
status_RedLED_Working = False

try:
	GPIO.output(GreenLED, GPIO.LOW)
	GPIO.output(YelloLED, GPIO.LOW)	
	
	SWG = status_GreenLED_Working
	SWR = status_RedLED_Working
	
	while True:
		
		if SWG == False:
			print ("\n====================")
			print ("\nSwicth Green case: 1")
			print ("\nStatus GreenLED Working = False")
			print ("\nGreen LED: ON")
		
			while SWG == False:	
			
				if GPIO.input(SwicthButtonGreen):
						
					GPIO.output(GreenLED, GPIO.HIGH)
					print("\nGreen LED Working... ON")
					time.sleep(0.1)
						
					GPIO.output(GreenLED, GPIO.LOW)
					print("Green LED Working... OFF")
					time.sleep(0.1)
					
			
				else:
					print ("\nStatus GreenLED Working = True")
					SWG = True
					GPIO.output(GreenLED, GPIO.LOW)
					print("Green LED: OFF")
						
				time.sleep(0.1)
						
		# ==============================================================		
				
		if SWG == True and SWR == False:	
			print ("\n====================")
			print ("\nSwicth Green case: 2")
			print ("\nStatus GreenLED Working = True")
			print ("\nBlue LED: ON")	
		
			while SWG == True:
				time.sleep(1)
				if GPIO.input(SwicthButtonGreen):
						
					GPIO.output(YelloLED, GPIO.HIGH)
					print("\nBlue LED Working... ON")
					time.sleep(0.1)
						
					GPIO.output(YelloLED, GPIO.LOW)
					print("Blue LED Working... OFF")
					time.sleep(0.1)
					
			
				else:
					print ("\nStatus GreenLED Working = False")
					SWG = False
					GPIO.output(YelloLED, GPIO.LOW)
					print("Blue LED: OFF")
						
				time.sleep(0.1)
		
		# ==============================================================
		if SWG == False and SWR == False:
			print ("\n====================")
			print ("\nSwicth Red case: 1")
			print ("\nStatus GreenLED Working = False")
			print ("\nGreen LED: ON")
		
			while SWR == False:	
			
				if GPIO.input(SwicthButtonRed):
						
					GPIO.output(GreenLED, GPIO.HIGH)
					print("\nGreen LED Working... ON")
					time.sleep(0.1)
						
					GPIO.output(GreenLED, GPIO.LOW)
					print("Green LED Working... OFF")
					time.sleep(0.1)
					
			
				else:
					GPIO.output(GreenLED, GPIO.LOW) #close LED
					SWR = True
					
					
				time.sleep(0.1)
						
		
		# ==============================================================
		if SWG == False or SWG == True or SWR == False :
				
			print ("\n====================")
			print ("\nSwicth Red case: 2\n")
			print ("Status GreenLED Working = False")
			print ("Status RedLED Working = True")
			print ("\nGreen LED: ON")
			
			while SWR == True:	
			
				if GPIO.input(SwicthButtonGreen):
						
					GPIO.output(GreenLED, GPIO.HIGH)
			
				else:
					GPIO.output(GreenLED, GPIO.LOW) #close LED
					SWR = False
					
				time.sleep(0.1)
		
		
		
		
finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
