from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import multiprocessing as mp
import Adafruit_PCA9685
import numpy as np
import cv2
import dlib
import math 
import time
import os
#import drivers
import Ultrasonict

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,200)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

pwm = Adafruit_PCA9685.PCA9685()

print("Run file SetDegree.py")

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    pwm.set_pwm(channel, 1, pulse)
    pwm.set_pwm(channel, 2, pulse)
    pwm.set_pwm(channel, 3, pulse)
    pwm.set_pwm(channel, 4, pulse)

pwm.set_pwm_freq(60)

''' convert pulse to degree 
    variable a Is Channel
    variable b To 0, don't need to pay attention
    variable c Is Degree
    
    # servo_min 	= 100 Hz is 0   degree
    # servo_Almostmax 	= 600 Hz is 180 degree
    # servo_max 	= 700 Hz is 252 degree

    # 0 degree = 100 Hz
    # 15 degree = 142 Hz
    # 30 degree = 183 Hz
    # 45 degree = 225 Hz
    # 90 degree = 350 Hz
    # 135 degree = 475 Hz
    # 180 degree = 600 Hz
    
    #***
    # 1 degree = 2.77 Hz
'''

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

	if distance >= 8:
	    print "Run Ultrasonict function Camera \n"
	    time.sleep(0.5)

	cv2.imshow("Frame", frame)

	key = cv2.waitKey(1)
	if key == 27:
	    break
