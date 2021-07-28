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

print("GPIO Version "+GPIO.VERSION)
print("Start Project ....")

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


def WorkingArmRoBot():
	command = "python Servo.py"
	os.system(command)
	print("Run file Servo.py ")
	global isWorking 
	isWorking = False
	return isWorking
	
	

try:
	print("Strat Camera Process ...")
	while True:
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
			'''
			if isWorking == False :
				if distance >= 12 :
					
					print "Distance mouth :",distance
					isWorking = True
					print "Run servo armrobot"
					Thread(target=WorkingArmRoBot).start()
						
						#if(__name__=='__main__'):
						#	p1 = mp.Process(target=WorkingArmRoBot())
						#	p1.start()
				else:
					print "Distance mouth :",distance
			'''	
			'''
			show message "IS WORK ARM ROBOT ..."
			#else:
				# print "IS WORKING ARM ROBOT ..."
			'''
			# ==========================================================
			#Setup Start Project 
			if statusButton_Green == 0 and statusButton_Red == 0 and statusButton_Emergent ==0:
				statusWorking_LEDGreen = 1
				statusWorking_LEDYello = 0
				statusButton_Green = 0
				statusButton_Red = 0
				statusButton_Emergent = 0
				dp.ready()
				
				if statusWorking_LEDGreen == 1:
					def Working_GreedLED():
						GPIO.output(LED_Green, GPIO.HIGH)
						print("\nGreen LED Working... ON")
						time.sleep(1)
										
						GPIO.output(LED_Green, GPIO.LOW)
						print("Green LED Working... OFF")
						time.sleep(1)
						
					Thread(target=Working_GreedLED).start()
		
			# ==========================================================
			
			#onClick Button Green
			if GPIO.input(OnClick_ButtonGreen) == 1 :
				statusWorking_LEDGreen = 0
				statusWorking_LEDYello = 1
				statusButton_Green = 1
				statusButton_Red = 0
				statusButton_Emergent = 0
				
			# ==========================================================
				
			if statusButton_Emergent == 0 and statusButton_Red != 1 and statusWorking_LEDYello == 1:
				print("111")
				dp.onClickButtonGreen()
				GPIO.output(LED_Green, GPIO.LOW)
				GPIO.output(LED_Green, GPIO.LOW)
						
				if isWorking == False :
					if distance >= 9:
						
						#print "Distance mouth :",distance
						#isWorking = True
						print "Run servo armrobot"
						#Thread(target=WorkingArmRoBot).start()
							
							#if(__name__=='__main__'):
							#	p1 = mp.Process(target=WorkingArmRoBot())
							#	p1.start()
							
					else:
						print "Distance mouth :"+str(distance)
						
						def Working_YelloLED():
							GPIO.output(LED_Yello, GPIO.HIGH)
							print("\nYello LED Working... ON")
							time.sleep(1)
										
							GPIO.output(LED_Yello, GPIO.LOW)
							print("Yello LED Working... OFF\n")
							time.sleep(1)
							
						Thread(target=Working_YelloLED).start()
		
			# ==========================================================
				
			'''
			#onClick Button Green But statusButton_Red have value 1
			if GPIO.input(OnClick_ButtonGreen) == 1 and statusButton_Red ==1 and statusButton_Emergent == 0:
					statusWorking_LEDGreen = 0
					statusWorking_LEDYello = 0
					statusButton_Green = 0
					statusButton_Red = 0
					statusButton_Emergent = 0
				
					GPIO.output(LED_Green, GPIO.LOW)
					print("\nGreen LED Working... OFF\n")
			
			
			#onClick Button Red
			if GPIO.input(OnClick_ButtonRed) == 1:
				print("OnClick Button Red")
				statusWorking_LEDGreen = 1
				statusWorking_LEDYello = 0
				statusButton_Green = 0
				statusButton_Red = 1
				statusButton_Emergent = 0
				dp.onClickButtonRed()

				if statusButton_Red == 1:
					GPIO.output(LED_Green, GPIO.HIGH)
					statusWorking_LEDGreen = 1
					statusButton_Red = 1
					print("\nGreen LED Working... ON\n")	
				
				print("="*30)	
				
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
				
			# ==========================================================
				
			if statusButton_Emergent == 1 and statusWorking_LEDYello == 1:
				def EmergentON():
					GPIO.output(LED_Yello, GPIO.HIGH)
					print("\nYello LED Working... ON")
						
				Thread(target=EmergentON).start()
				
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
				
				print("\nOnClick Button Emergent: OFF\n")
				print("="*30)
				
			# ==========================================================
			
			else:
				print("\nstatus button Green: "+"."*9 +"\t"+str(statusButton_Green))
				print("status button Red: "+"."*11 +"\t"+str(statusButton_Red))
				print("status button Emergent: "+"."*6 +"\t"+str(statusButton_Emergent))
				print("\nstatus Working LED Green: "+"."*4 +"\t"+str(statusWorking_LEDGreen))
				print("status Working LED Red: "+"."*6 +"\t"+str(statusWorking_LEDYello)+"\n")
				print("="*30)
		
			time.sleep(0.001)
			
			# ==========================================================
		
		
		cv2.imshow("Frame", frame)

		key = cv2.waitKey(1)
		if key == 27:
			break

finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
