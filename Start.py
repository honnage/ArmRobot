from __future__ import division
from threading import Thread
import multiprocessing as mp
import RPi.GPIO as GPIO
import DisplayLCD  as dp
import cv2
import numpy as np
import dlib
import math 
import time
import os
import SetDegree as sd

sd.default()
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

# --- CV2 and Dlib ----
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,200)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

isWorking = False
status_arm = 0

def Working_GreedLED():
	GPIO.output(LED_Green, GPIO.HIGH)
	print("\nGreen LED Working... ON")
	time.sleep(1)
						
	GPIO.output(LED_Green, GPIO.LOW)
	print("Green LED Working... OFF")
	time.sleep(1)
	

def EmergentON():
	GPIO.output(LED_Yello, GPIO.HIGH)
	print("\nYello LED Working... ON")
	time.sleep(0.1)
	

try:
	print ("Sound on")
	command = "aplay Sound_Power-on.wav"
	os.system(command)
	
	GPIO.output(LED_Green, GPIO.LOW)
	GPIO.output(LED_Yello, GPIO.LOW)
	print("Strat Camera Process ...")
	dp.ready()
	
	while True:
		sd.default()
		GPIO.output(LED_Green, GPIO.LOW)
		GPIO.output(LED_Yello, GPIO.LOW)
				
		_, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = detector(gray)
		for face in faces:
			x1 = face.left()
			y1 = face.top()
			x2 = face.right()
			y2 = face.bottom()
			#cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

			landmarks = predictor(gray, face)

			TOP_X = landmarks.part(62).x
			TOP_Y = landmarks.part(62).y
			BOTTOM_X = landmarks.part(66).x
			BOTTOM_Y = landmarks.part(66).y
			cv2.circle(frame, (TOP_X, TOP_Y), 2, (255,0,0), -1)
			cv2.circle(frame, (BOTTOM_X, BOTTOM_Y), 2, (0,0,255), -1)
							
			p1 = [TOP_X,TOP_Y]
			p2 = [BOTTOM_X,BOTTOM_Y]
			distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

		
			#Working Servo Motor if distance >= 7 cm
			if isWorking == False and status_arm == 0 :
				statusWorking_LEDGreen = 1
				statusWorking_LEDYello = 0
				statusButton_Green = 0
				statusButton_Red = 0
				statusButton_Emergent = 0
				dp.ready()
				
				
				if distance >= 1 and statusWorking_LEDGreen == 1 and statusButton_Emergent == 0:
					Thread(target=Working_GreedLED).start()
						
					if distance >= 7 :
						print "Distance mouth :",distance
						distance = 0
						status_arm = 1
						isWorking = True
						cv2.imshow("Frame", frame)
						distance = 0
						print("Run file Servo.py ")
						command = "python Servo.py"
						os.system(command)
						
					else:
						print "Distance mouth :",distance
	
				else:
					print "Distance mouth :",distance
			
			
			#Close Process Servo Motor and reset working
			if isWorking == True and distance >= 7 :
				sd.default()
				if status_arm == 1:
					status_arm = 0
					print("\n")
					print("="*20)
					print("\nReset Camera\n")
					print("="*20)
					time.sleep(0.5)
				
				if status_arm == 0:
					isWorking = False
					distance = 0
					print("200")
					time.sleep(1)
					for i in range(10):
						cv2.imshow("Frame", frame)
						time.sleep(0.2)
				time.sleep(1)
				
			
			#onClick Button Green
			if GPIO.input(OnClick_ButtonGreen) == 1 :
				isWorking = True
				print("Run file Servo.py ")
				command = "python Servo.py"
				os.system(command)
				
				
			#onClick Button Red
			'''
			if GPIO.input(OnClick_ButtonRed) == 1:
				print("OnClick Button Red")
				print ("Sound on")
				command = "aplay Sound_Shutdown.wav"
				os.system(command)
				exit()	
			'''
			
			#onClick Button Emergent: ON 
			if GPIO.input(Onclick_ButtonEmergent) == 0:
				statusWorking_LEDGreen = 0
				statusWorking_LEDYello = 1
				statusButton_Green = 0
				statusButton_Red = 0
				statusButton_Emergent = 1
				
				GPIO.output(LED_Green, GPIO.LOW)
				GPIO.output(LED_Yello, GPIO.LOW)
				dp.onClickButtonEmergency_on()
				EmergentON()
				time.sleep(1)
				
			if statusButton_Emergent == 1 and statusWorking_LEDYello == 1:
				Thread(target=EmergentON).start()

			
			if GPIO.input(OnClick_ButtonGreen) == 1 and  statusButton_Emergent == 1:
				pass
				
					
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
		
		
		cv2.imshow("Frame", frame)

		key = cv2.waitKey(1)
		if key == 27:
			break

finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
