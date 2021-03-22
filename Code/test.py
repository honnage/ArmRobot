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
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def calDeg(a,b,c):
	re_deg = c
	degree = 2.77*c
	degree = degree+100
	degree = int(degree)
	pwm.set_pwm(a,b,degree)
	return re_deg

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#function default
def default():
    calDeg(0, 0, 10)
    calDeg(1, 0, 15)
    calDeg(2, 0, 0)
    calDeg(3, 0, 85)
    calDeg(4, 0, 90)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	
def default_takkao():
    def default_takkao_channel1(): #servo channel 1
	for i in range(20, 45, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.01)

    def default_takkao_channel2(): #servo channel 2
	for i in range(10, 40, 1):
	    calDeg(2, 0, i)
	    time.sleep(0.01)
   
    def default_takkao_channel3(): #servo channel 3
	for i in range(60, 90, 1):
	    calDeg(3, 0, i)
	    time.sleep(0.01)
    
    calDeg(0, 0, 10)
    calDeg(1, 0, 20)
    calDeg(2, 0, 10)
    calDeg(3, 0, 60)
    calDeg(4, 0, 0)
    default_takkao_channel2()
    default_takkao_channel1()
    default_takkao_channel3()

    time.sleep(0.5)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def scoop_rice():
    def scoop_rice_channel1(): #servo channel 1
	for i in range(45, 60, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.01)
	    
    def scoop_rice_channel3(): #servo channel 3
	for i in range(90, 140, 1):
	    calDeg(3, 0, i)
	    time.sleep(0.01)

    def scoop_rice_channel4(): #servo channel 4
	for i in range(0, 90, 1):
	    calDeg(4, 0, i)
	    time.sleep(0.01)
    
    calDeg(0, 0, 10)
    calDeg(1, 0, 45)
    calDeg(2, 0, 42)
    calDeg(3, 0, 90)
    calDeg(4, 0, 0)
    
    scoop_rice_channel1()
    scoop_rice_channel3()
    scoop_rice_channel4()
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def scoop_rice_default():    
    def scoop_rice_default_channel3(): #servo channel 3
	for i in range(140, 90, -1):
	    calDeg(3, 0, i)
	    time.sleep(0.05)
	   
    calDeg(0, 0, 10)
    calDeg(1, 0, 60)
    calDeg(2, 0, 42)
    calDeg(3, 0, 140)
    calDeg(4, 0, 90)
    scoop_rice_default_channel3()
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx	    
	    
def make_angle():
    def make_angle_channel1(): #servo channel 1
	for i in range(60, 90, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.03)
		
    def make_angle_channel2(): #servo channel 2
	for i in range(42, 80, 1):
	    calDeg(2, 0, i)
	    time.sleep(0.03)
    
    #calDeg(0, 0, 10)
    calDeg(1, 0, 90)
    calDeg(2, 0, 80)
    calDeg(3, 0, 90)
    calDeg(4, 0, 90)
    
   # make_angle_channel1()
   # make_angle_channel2()
    
    
    if(__name__=='__main__'):
	p1 = mp.Process(target=make_angle_channel1)
	p2 = mp.Process(target=make_angle_channel2)
	p1.start()
	p2.start()
    time.sleep(0.05)
    
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def arm2user():
    calDeg(1, 0, 90)
    calDeg(2, 0, 80)
    calDeg(3, 0, 90)
    print "arm to user"
    for i in range(0, 90, 1):
	calDeg(0, 0, i)

	time.sleep(0.03)
    time.sleep(1)
    
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def arm2user_fit():
    calDeg(0, 0, 90)
    calDeg(1, 0, 90)
    calDeg(2, 0, 80)
    calDeg(3, 0, 90)
    calDeg(4, 0, 90)
    print 'arm to user fit'
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
def re_standby():
    calDeg(1, 0, 60)
    calDeg(2, 0, 42)
    calDeg(3, 0, 90)
    for i in range(90, 0, -1):
	calDeg(0,0,i)
	time.sleep(0.01)
    time.sleep(1)
    
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#function default
def re_default():
    def re_default_channel1(): #servo channel 1
	for i in range(60, 15, -1):
	    calDeg(1, 0, i)
	    time.sleep(0.03)
	
    def re_default_channel2(): #servo channel 2
	for i in range(42, 0, -1):
	    calDeg(2, 0, i)
	    time.sleep(0.03)
    
    def re_default_channel3(): #servo channel 3
	for i in range(90, 85, -1):
	    calDeg(3, 0, i)
	    time.sleep(0.03)
	    
    time.sleep(0.05)
    calDeg(1, 0, 60)
    calDeg(2, 0, 42)
    calDeg(3, 0, 90)
    calDeg(4, 0, 90)
    
    if(__name__=='__main__'):
        p1 = mp.Process(target=re_default_channel1)
        p2 = mp.Process(target=re_default_channel2)
	p3 = mp.Process(target=re_default_channel3)
        p1.start()
        p2.start()
	p3.start()
   
    print "re d"
	
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def main():
    print('Moving servo on channel 0, press Ctrl-C to quit...')
    time.sleep(1)
    default()
    time.sleep(1)
    default_takkao()
    #----
    scoop_rice() 
    scoop_rice_default()
    time.sleep(0.003)
    print("problem1")
    make_angle() #problem1
    time.sleep(0.001)
    arm2user()
    time.sleep(0.001)
    arm2user_fit()
    
    time.sleep(0.01)
    calDeg(1, 0, 90)
    calDeg(2, 0, 80)
    
    ser1 = calDeg(1, 0, 90)
    ser2 = calDeg(2, 0, 80)
    
    arm_dis = Ultrasonict.check_extra()

    while arm_dis >= 20:
	arm_dis = Ultrasonict.check_extra()
	print(arm_dis)
	ser1 += 1
	print(ser1)
	ser2 += 1
	print(ser2)
	calDeg(1, 0, ser1)
	time.sleep(0.005)
	calDeg(2, 0, ser2)
	time.sleep(0.005)

    time.sleep(3)

    arm_dis = Ultrasonict.check_extra()
    while arm_dis < 20:
	arm_dis = Ultrasonict.check_extra()
	
    arm2user_fit()
    time.sleep(0.005)
    re_standby()
    re_default()
    time.sleep(0.5)
    default()
    time.sleep(1)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

'''
calDeg(3, 0, 180)
print "c"
calDeg(0, 0, 20)
'''
#while True:
#main()

    

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
                print "Run Ultrasonict function Camera \n"
                time.sleep(0.5)
                #Ultrasonict.Arm()
                main()
                GPIO.cleanup()
                print "camera"
        
                        
        

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
