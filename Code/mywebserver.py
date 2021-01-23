from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import cv2
import numpy as np
import dlib
import math 
import time
import os
import drivers
import Ultrasonict 
import time
import Adafruit_PCA9685
import multiprocessing as mp
import SetDistance as SetD
import FaceCV
import Servo

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,200)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

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
		print "Distance mouth :",distance
		
		
		if distance >= 4:
			a = 0
			print "Run Ultrasonict function Camera \n"
			servo_time = 0.001

			a = Ultrasonict.Camera()

			Servo.default()
			time.sleep(1)
			Servo.default_takkao()
			Servo.scoop_rice()
			sServo.coop_rice_default()
			time.sleep(0.5)
			Servo.arm2user()
			time.sleep(1)
			Servo.arm2user_fit()
			
			
		time.sleep(0.5)
		
		
	cv2.imshow("Frame", frame)

	key = cv2.waitKey(1)
	if key == 27:
		break
