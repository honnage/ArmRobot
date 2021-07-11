from __future__ import division
from threading import Thread
import multiprocessing as mp
import RPi.GPIO as GPIO
import time
import os

print(GPIO.VERSION)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_Green = 14 #Purple
LED_YelloLED = 17 #Purple

SwicthButtonGreen = 15 #Yello
SwicthButtonRed = 18 #Blue

GPIO.setup(14, GPIO.OUT)
GPIO.setup(LED_YelloLED, GPIO.OUT)


GPIO.setup(SwicthButtonGreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SwicthButtonRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


status_SwicthGreen = 0
status_SwicthRed = 0

status_case1 = "T"
status_case2 = "F"
try:
	
	
	GPIO.output(LED_Green, GPIO.LOW)
	GPIO.output(LED_YelloLED, GPIO.LOW)	
	
	while 1:
		
		if status_SwicthGreen == 0:
			#status_case1 = "T"
			print ("\ncase: 1")
			print ("status_SwicthGreen: "+str(status_SwicthGreen))
			print ("status_SwicthRed: "+str(status_SwicthRed))
			print ("status_case1: "+str(status_case1))
			print ("status_case2: "+str(status_case2)+"\n")
			
			
			while status_SwicthGreen == 0:
				if GPIO.input(SwicthButtonGreen) == 0 and status_case2 != "T":
					
					GPIO.output(LED_Green, GPIO.HIGH)
					print("\nGreen LED Working... ON")
					time.sleep(1)
						
					GPIO.output(LED_Green, GPIO.LOW)
					print("Green LED Working... OFF")
					time.sleep(1)
					
			
				if GPIO.input(SwicthButtonGreen) == 1 :
					GPIO.output(LED_Green, GPIO.LOW)
					status_SwicthGreen = 1
					status_case1 = "F"
					
					
					print ("\nstatus_SwicthGreen: "+str(status_SwicthGreen))
					print ("status_SwicthRed: "+str(status_SwicthRed))
					print ("status_case1: "+str(status_case1))
					print ("status_case2: "+str(status_case2))
					print("Green LED: OFF")
					print("\n=========================================")
					
					
				if GPIO.input(SwicthButtonRed) == 1:
					if status_SwicthRed == 0:
						GPIO.output(LED_Green, 1)
						GPIO.output(LED_YelloLED, 0)
						status_SwicthRed = 1
						status_SwicthGreen = 1
						status_case1 = "F"
						print("Status Swicth Red: "+str(status_SwicthRed))
						print("LED RED: OFF\n")
					
					else:
						'''
						GPIO.output(LED_YelloLED, 0)
						status_SwicthRed = 1
						status_SwicthGreen = 1
						status_case1 = "F"
						print("Status Swicth Red: "+str(status_SwicthRed))
						'''
						print("LED RED: OFF\n")
						
				time.sleep(0.1)
						
				
				
		
		if GPIO.input(SwicthButtonGreen) == 1:
			print ("\ncase: 2")
			status_case2 = "T"
			print ("status_SwicthGreen: "+str(status_SwicthGreen))
			print ("status_SwicthRed: "+str(status_SwicthRed))
			print ("status_case1: "+str(status_case1))
			print ("status_case2: "+str(status_case2)+"\n")
			
			while status_SwicthGreen == 1:
				if status_case2 == "T":

					if status_SwicthGreen == 1:
						GPIO.output(LED_YelloLED, GPIO.HIGH)
						print("\nYello LED Working... ON")
						time.sleep(1)
							
						GPIO.output(LED_YelloLED, GPIO.LOW)
						print("Yello LED Working... OFF")
						time.sleep(1)
				
				
				if GPIO.input(SwicthButtonRed) == 1 :
					GPIO.output(LED_YelloLED, GPIO.LOW)
					status_SwicthGreen = 0
					status_case2 == "T"
					print ("\nstatus_SwicthGreen: "+str(status_SwicthGreen))
					print ("status_SwicthRed: "+str(status_SwicthRed))
					print ("status_case1: "+str(status_case1))
					print ("status_case2: "+str(status_case2))
					print("Yello LED: OFF")
					print("\n=========================================")
					
		
				
	
					
		
		
		
		
finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
