from __future__ import division
from threading import Thread
import multiprocessing as mp
import RPi.GPIO as GPIO
import math 
import time
import os


print("GPIO Version "+GPIO.VERSION)
print("Start Project ....")
GPIO.cleanup()
	
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# --- Set GPIO ---
LED_Green = 27 #Green
LED_Yello = 22 #Yello

OnClick_ButtonGreen = 23 #Orange
OnClick_ButtonRed = 24 #Yello
Onclick_ButtonEmergent = 4 #Broen 

GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(LED_Yello, GPIO.OUT)


GPIO.setup(OnClick_ButtonGreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(OnClick_ButtonRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Onclick_ButtonEmergent, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

statusWorking_LEDGreen = 0
statusWorking_LEDYello = 0

statusButton_Green = 0
statusButton_Red = 0
statusButton_Emergent = 0



def WorkingCamera():
	command = "python FaceCV.py"
	os.system(command)
	print("Run file FaceCV.py")
	global isWorking 
	isWorking = False
	return isWorking
	
try:
	GPIO.output(LED_Green, GPIO.LOW)
	GPIO.output(LED_Yello, GPIO.LOW)
	print("Strat Camera Process ...")

	
	while True:
	
		#Setup Start Project 
		if statusButton_Emergent == 0 and statusButton_Red == 0 and statusWorking_LEDYello == 0 and statusButton_Green == 0:
			statusWorking_LEDGreen = 1
			statusWorking_LEDYello = 0
			statusButton_Green = 0
			statusButton_Red = 0
			statusButton_Emergent = 0
			
			isWorking = False	
				
			if isWorking == False :

				if statusWorking_LEDGreen == 1:
					GPIO.output(LED_Green, GPIO.HIGH)
					print("\nGreen LED Working... ON")
					time.sleep(1)
											
					GPIO.output(LED_Green, GPIO.LOW)
					print("Green LED Working... OFF")
					time.sleep(1)
		# ==========================================================
		#onClick Button Green
		if GPIO.input(OnClick_ButtonGreen) == 1 :
			isWorking = True
			time.sleep(1)
	
			Thread(target=WorkingCamera).start()
				
			statusWorking_LEDGreen = 0
			statusWorking_LEDYello = 1
			statusButton_Green = 1
			statusButton_Red = 0
			statusButton_Emergent = 0
		# ==========================================================
		if isWorking == True and statusWorking_LEDYello == 1 and statusButton_Green == 1:
			GPIO.output(LED_Yello, GPIO.HIGH)
			print("Yello LED Working... ON")
			time.sleep(1)
											
			GPIO.output(LED_Yello, GPIO.LOW)
			print("Yello LED Working... OFF")
			time.sleep(1)
		# ==========================================================
		#onClick Button Red
		if GPIO.input(OnClick_ButtonRed) == 1:
			print("OnClick Button Red")
			exit()	
		# ==========================================================
		#onClick Button Emergent: ON 
		if GPIO.input(Onclick_ButtonEmergent) == 0:
			statusWorking_LEDGreen = 0
			statusWorking_LEDYello = 1
			statusButton_Green = 0
			statusButton_Red = 0
			statusButton_Emergent = 1
				
			GPIO.output(LED_Green, GPIO.LOW)
			GPIO.output(LED_Yello, GPIO.LOW)
			if statusButton_Emergent == 1:
				GPIO.output(LED_Yello, GPIO.HIGH)
				print("\Yello LED Working... ON")
				time.sleep(0.1)
											
				GPIO.output(LED_Yello, GPIO.LOW)
				print("Yello LED Working... OFF")
				time.sleep(0.1)
		# ==========================================================
		if statusButton_Emergent == 1 and statusWorking_LEDYello == 1:
			pass
		# ==========================================================
		if GPIO.input(OnClick_ButtonGreen) == 1 and  statusButton_Emergent == 1:
			pass	
		# ==========================================================
					
		#onClick Button Emergent: OFF	
		if GPIO.input(Onclick_ButtonEmergent) == 1 and  statusButton_Emergent == 1:
			statusWorking_LEDGreen = 0
			statusWorking_LEDYello = 0
			statusButton_Green = 0
			statusButton_Red = 0
			statusButton_Emergent = 0
			GPIO.output(LED_Green, GPIO.LOW)
			GPIO.output(LED_Yello, GPIO.LOW)
				
			print("\nOnClick Button Emergent: OFF\n")
			print("="*30)
				
		# ==========================================================
		'''
		else:
			print("\nstatus button Green: "+"."*9 +"\t"+str(statusButton_Green))
			print("status button Red: "+"."*11 +"\t"+str(statusButton_Red))
			print("status button Emergent: "+"."*6 +"\t"+str(statusButton_Emergent))
			print("\nstatus Working LED Green: "+"."*4 +"\t"+str(statusWorking_LEDGreen))
			print("status Working LED Red: "+"."*6 +"\t"+str(statusWorking_LEDYello)+"\n")
			print("="*30)
		
		time.sleep(0.001)
		'''
		# ==========================================================
		
		


finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
