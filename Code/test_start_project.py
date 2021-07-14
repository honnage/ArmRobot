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
LED_Yello = 17 #Purple

SwicthButtonGreen = 15 #Yello
SwicthButtonRed = 18 #Blue

GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(LED_Yello, GPIO.OUT)


GPIO.setup(SwicthButtonGreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SwicthButtonRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


StatusWorking_LEDGreen = 0
statusWorking_LEDYello = 0

statusButton_Green = False
statusButton_Red = False


def exit_ButtonGreen(button):
	global statusButton_Green
	statusButton_Green = 0

def exit_ButtonRed(button):
	global statusButton_Red
	statusButton_Red = 0

GPIO.add_event_detect(SwicthButtonGreen, GPIO.FALLING, callback=exit_ButtonGreen, bouncetime=300)
GPIO.add_event_detect(SwicthButtonRed, GPIO.FALLING, callback=exit_ButtonRed, bouncetime=300)

isWorking = False 

def runfile_test():
	command = "python runfile_test.py"
	os.system(command)
	print("Run file runfile_test.py ")
	global isWorking 
	isWorking = False
	print("isWorking "+str(isWorking))
	return isWorking

def stop_run():
	command = "^C"
	isWorking = False
	return isWorking
	
try:
	GPIO.output(LED_Green, GPIO.LOW)
	GPIO.output(LED_Yello, GPIO.LOW)	
	
	print("\nStatus Working LED Green is " + str(StatusWorking_LEDGreen))
	print("Status Working LED Yello is " + str(statusWorking_LEDYello))
	
	while statusButton_Green or statusButton_Red or True:
		
		if StatusWorking_LEDGreen == 0:
			print("\nStatusWorking_LEDGreen is 1/HIGH/True")
		
			while StatusWorking_LEDGreen == 0 and statusButton_Green == False: 
				if StatusWorking_LEDGreen == 0 and statusButton_Green == False :
					GPIO.output(LED_Green, GPIO.HIGH)
					print("\nGreen LED Working... ON")
					time.sleep(1)
								
					GPIO.output(LED_Green, GPIO.LOW)
					print("Green LED Working... OFF")
					time.sleep(1)
					
				
				if GPIO.input(SwicthButtonGreen) == 1 :
					GPIO.output(LED_Green, GPIO.LOW)
					StatusWorking_LEDGreen = 0;
					StatusWorking_LEDYello = 1;
					statusButton_Green = True
					statusButton_Red = False
				
				if GPIO.input(SwicthButtonRed) == 1 :
					GPIO.output(LED_Green, GPIO.HIGH)
					StatusWorking_LEDGreen = 1;
					StatusWorking_LEDYello = 0;
					statusButton_Green = False
					statusButton_Red = True
				
				time.sleep(0.1)
		
		
		
		if statusButton_Green == True and statusButton_Red == False:
			print("OnClick Button Grren")
			print("\nStatusWorking_LEDYello is 1/HIGH/True")
			
			
			if isWorking == False :
				isWorking = True
				print "Run servo armrobot"
				Thread(target=runfile_test).start()
						

			
			while StatusWorking_LEDYello == 1: 
				
				if StatusWorking_LEDYello == 1 and isWorking == True:
					GPIO.output(LED_Yello, GPIO.HIGH)
					print("\nYello LED Working... ON")
					time.sleep(1)
								
					GPIO.output(LED_Yello, GPIO.LOW)
					print("Yello LED Working... OFF")
					time.sleep(1)
					
				
				if StatusWorking_LEDYello == 1 and isWorking == False:
					GPIO.output(LED_Green, GPIO.LOW)
					StatusWorking_LEDGreen = 0;
					StatusWorking_LEDYello = 0;
					statusButton_Green = False
					statusButton_Red = False
					print("\nStatusWorking_LEDYeelo is 0/LOW/False")
					print("\n========================================")
					
					
				if GPIO.input(SwicthButtonRed) == 1 :
					#Thread(target=stop_run).start()
					GPIO.output(LED_Green, GPIO.HIGH)
					StatusWorking_LEDGreen = 1;
					StatusWorking_LEDYello = 0;
					statusButton_Green = False
					statusButton_Red = True
					print("\nStatusWorking_LEDYeelo is 0/LOW/False")
					print("\n========================================")
			
			
					
		if statusButton_Green == False and statusButton_Red == True:
			print("OnClick Button Red")
			print("\nStatusWorking_LEDGreen is 1/HIGH/True")
			
			while StatusWorking_LEDGreen == 1: 
				if StatusWorking_LEDGreen == 1:
					GPIO.output(LED_Green, GPIO.HIGH)
					print("\nGreen LED Working... ON")
					time.sleep(1)
					
								
				if GPIO.input(SwicthButtonGreen) == 1 :
					GPIO.output(LED_Green, GPIO.LOW)
					StatusWorking_LEDGreen = 0;
					StatusWorking_LEDYello = 0;
					statusButton_Green = False
					statusButton_Red = False
					print("\n========================================")
					
			time.sleep(0.1)
		
		
		
finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
