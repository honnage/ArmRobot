from __future__ import division
from threading import Thread
import multiprocessing as mp
import RPi.GPIO as GPIO
import cv2
import numpy as np
import dlib
import math 
import time
import os
print("Start Project ....")
print(GPIO.VERSION)

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

# --- Set Status ---
statusWorking_LEDGreen = 0
statusWorking_LEDYello = 0

statusButton_Green = 0
statusButton_Red = 0
statusButton_Emergent = 0

isWorking = False 
 
 
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,200)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def runfile_test():
	command = "python runfile_test.py"
	os.system(command)
	print("Run file runfile_test.py ")
	global isWorking 
	isWorking = False
	print("isWorking "+str(isWorking))
	return isWorking

try:
	print ("Sound on")
	command = "aplay Sound_Power-on.wav"
	os.system(command)
		
	GPIO.output(LED_Green, GPIO.LOW)
	GPIO.output(LED_Yello, GPIO.LOW)	
	GPIO.cleanup()


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
			
			if isWorking == False :
				if distance >= 12 :
				
					print "Distance mouth :",distance
					'''
					isWorking = True
					print "Run servo armrobot"
					Thread(target=WorkingArmRoBot).start()
						
						#if(__name__=='__main__'):
						#	p1 = mp.Process(target=WorkingArmRoBot())
						#	p1.start()
					'''
				else:
					print "Distance mouth :",distance
				
		cv2.imshow("Frame", frame)

		key = cv2.waitKey(1)
		if key == 27:
			break
			
	    
finally:
	GPIO.cleanup()
	print("\n\nclean up")
	time.sleep(3)
