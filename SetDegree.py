from __future__ import division
import time
import math
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import multiprocessing as mp
import os

pwm = Adafruit_PCA9685.PCA9685()

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
def calDeg(a,b,c):
	re_deg = c
	degree = 2.77*c
	degree = degree+100
	degree = int(degree)
	pwm.set_pwm(a,b,degree)
	return re_deg
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def default():
    #print("Function: Set Degree Servo Default")
    calDeg(0, 0, 10)
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 85)
    calDeg(4, 4, 90)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def default_low():
    print("Function: Set Degree default low")
    calDeg(0, 0, 10)
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 85)
    calDeg(4, 4, 90)
    
    def default_low_channel1(): #servo channel 0
	for i in range(90, 20, -1):
	    calDeg(1, 1, i)
	    time.sleep(0.01)
	    
    def default_low_channel2(): #servo channel 0
	for i in range(90, 0, -1):
	    calDeg(2, 2, i)
	    time.sleep(0.01)
	    
    if(__name__=='__main__'):
	p2 = mp.Process(target=default_low_channel2)
	p1 = mp.Process(target=default_low_channel1)
	
	p2.start()
	p1.start()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def default_rice():
    def default_rice_channel1(): #servo channel 1
	for i in range(20, 45, 1):
	    calDeg(1, 1, i)
	    time.sleep(0.02)

    def default_rice_channel2(): #servo channel 2
	for i in range(10, 50, 1):
	    calDeg(2, 2, i)
	    time.sleep(0.02)
	    #print("deg servo 2 "+str(i))
   
    def default_rice_channel3(): #servo channel 3
	for i in range(60, 90, 1):
	    calDeg(3, 3, i)
	    time.sleep(0.02)
	    
    print ("Function: default rice")
    calDeg(0, 0, 10)
    calDeg(1, 1, 20)
    calDeg(2, 2, 10)
    calDeg(3, 3, 60)
    calDeg(4, 4, 0)
    
    default_rice_channel2()
    default_rice_channel1()
    default_rice_channel3()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def scoop_rice():
    def scoop_rice_channel1(): #servo channel 1
	for i in range(45, 90, 1):
	    calDeg(1, 1, i)
	    time.sleep(0.02)
	    
    def scoop_rice_channel3(): #servo channel 3
	for i in range(90, 140, 1):
	    calDeg(3, 3, i)
	    time.sleep(0.02)
    
    def scoop_rice_channel4(): #servo channel 4
	for i in range(0, 90, 1):
	    calDeg(4, 4, i)
	    time.sleep(0.01)

    print ("Function: scoop rice")
    calDeg(0, 0, 10)
    calDeg(1, 1, 45)
    calDeg(2, 2, 50)
    calDeg(3, 3, 90)
    calDeg(4, 4, 0)
    
    if(__name__=='__main__'):
	p3 = mp.Process(target=scoop_rice_channel3)
	p1 = mp.Process(target=scoop_rice_channel1)
	p3.start()
	p1.start()
    
    time.sleep(0.5)
    scoop_rice_channel4()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def scoop_up():    
    print ("Function: scoop up")
    calDeg(0, 0, 10)
    calDeg(1, 1, 90)
    calDeg(2, 2, 50)
    calDeg(3, 3, 140)
    calDeg(4, 4, 90)
    
    def scoop_up_channel1(): #servo channel 1
	for i in range(90, 29, -1):
	    calDeg(1, 1, i)
	    print("servo 1 deg: "+str(i))
	    time.sleep(0.05)
	    
    def scoop_up_channel2(): #servo channel 2
	for i in range(50, 29, -1):
	    calDeg(2, 2, i)
	    print("servo 2 deg: "+str(i))
	    time.sleep(0.03)
	    
    def scoop_up_channel3(): #servo channel 3
	for i in range(141, 129, -1):
	    calDeg(3, 3, i)
	    print("servo 3 deg: "+str(i))
	    time.sleep(0.05)

    if(__name__=='__main__'):
	p3 = mp.Process(target=scoop_up_channel3)
	p2 = mp.Process(target=scoop_up_channel2)
	p1 = mp.Process(target=scoop_up_channel1)
	p3.start()
	p2.start()
	p1.start()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_scoop_up():
    calDeg(0, 0, 10)
    calDeg(1, 1, 29)
    calDeg(2, 2, 29)
    calDeg(3, 3, 129)
    calDeg(4, 4, 90)
    print 'Function: arm to fit scoop up'
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_corner_forward():
    def turn_corner_forward_channel0(): #servo channel 0
	for i in range(10, 90, 1):
	    calDeg(0, 0, i)
	    time.sleep(0.02)
	    
    print ("Function: turn corner forward")
    time.sleep(1)
    calDeg(0, 0, 10)
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    
    turn_corner_forward_channel0()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_turn_corner_forward():
    calDeg(0, 0, 90)
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    print 'Function: arm to fit turn corner forward'
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3):
    print '\nFunction: distance case'
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    
    start_servo1 = 30
    start_servo2 = 30
    start_servo3 = 130
    
    def distance_detail():
	
	print("\nDetail Servo working")
	print(loop_degServo1)
	print(loop_degServo2)
	print(loop_degServo3)
	
	for i in range(0, 21, 1):
	    degServo1 = start_servo1 + (loop_degServo1 * i)
	    degServo2 = start_servo2 + (loop_degServo2 * i)
	    degServo3 = start_servo3 + (loop_degServo3 * i)
	    print("N: " + str(i) + 
		"\t| servo 1: "+ str(degServo1) + 
		" ~ " + str(int(round(degServo1)))+
		"\t| servo 2: "+ str(degServo2) + 
		" ~ " + str(int(round(degServo2)))+
		"\t| servo 3: "+ str(degServo3) + 
		" ~ " + str(int(round(degServo3))))
	print("\n")
    
    time_speack = 0.05
    
    def distance_case_channel1(): #servo channel 1
	for i in range(0, 21, 1):
	    degServo1 = int(round(start_servo1 + (loop_degServo1 * i)))
	    calDeg(1, 1, degServo1)
	    print("servo 1: N: " + str(i) + "\t| servo 1: "+ str(degServo1))
	    time.sleep(time_speack)
    
    def distance_case_channel2(): #servo channel 2
	for i in range(0, 21, 1):
	    degServo2 = int(round(start_servo2 + (loop_degServo2 * i)))
	    calDeg(2, 2, degServo2)
	    print("servo 2: N: " + str(i) + "\t| servo 2: "+ str(degServo2))
	    time.sleep(time_speack)
    
    def distance_case_channel3(): #servo channel 3
	for i in range(0, 21, 1):
	    degServo3 = int(round(start_servo3 + (loop_degServo3 * i)))
	    calDeg(3, 3, degServo3)
	    print("servo 3: N: " + str(i) + "\t| servo 3: "+ str(degServo3))
	    time.sleep(time_speack)
    
    distance_detail()    
    if(__name__=='__main__'):
	p1 = mp.Process(target=distance_case_channel1)
	p2 = mp.Process(target=distance_case_channel2)
	p3 = mp.Process(target=distance_case_channel3)
	p1.start()
	p2.start()
	p3.start()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_cornerback(Servo1, Servo2):
    print 'Function: turn cornerback'
    Servo1 = int(Servo1)
    Servo2 = int(Servo2)
    
    print ("Value servo 1 = " + str(Servo1))
    print ("Value servo 2 = " + str(Servo2))
    
    def turn_cornerback_channel1(): #servo channel 1
	if(Servo1 < 151):
	    for i in range(Servo1, 30, -1):
		calDeg(1, 1, i)
		print("servo 1 deg: "+str(i))
		time.sleep(0.03)
	else:
	    for i in range(150, 30, -1):
		calDeg(1, 1, i)
		print("servo 1 deg: "+str(i))
		time.sleep(0.03)
		
    def turn_cornerback_channel2(): #servo channel 2
	if(Servo2 < 151):
	    for i in range(Servo2, 30, -1):
		calDeg(2, 2, i)
		print("servo 2 deg: "+str(i))
		time.sleep(0.03)
	else:
	    for i in range(150, 30, -1):
		calDeg(2, 2, i)
		print("servo 2 deg: "+str(i))
		time.sleep(0.03)
	
    calDeg(3, 3, 100)
    calDeg(4, 4, 90)

    if(__name__=='__main__'):
	p2 = mp.Process(target=turn_cornerback_channel2)
	p1 = mp.Process(target=turn_cornerback_channel1)
	p2.start()
	p1.start()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_turn_back():
    calDeg(0, 0, 90)
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    print 'Function: arm to fit turn_back'
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_back():
    def turn_back_channel0(): #servo channel 0
	for i in range(90, 10, -1):
	    calDeg(0, 0, i)
	    time.sleep(0.01)
    
    def turn_back_channel1(): #servo channel 1
	for i in range(30, 90, 1):
	    calDeg(1, 1, i)
	    time.sleep(0.01)
    
    def turn_back_channel2(): #servo channel 2
	for i in range(30, 90, 1):
	    calDeg(2, 2, i)
	    time.sleep(0.01)
	    
    def turn_back_channel3(): #servo channel 3
	for i in range(130, 85, -1):
	    calDeg(3, 3, i)
	    time.sleep(0.01)

    print ("Function: turn back")
    calDeg(0, 0, 90)
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    
    turn_back_channel3()
    time.sleep(0.05)
    turn_back_channel0()
    time.sleep(0.05)
    
    if(__name__=='__main__'):
	p2 = mp.Process(target=turn_back_channel2)
	p1 = mp.Process(target=turn_back_channel1)
	p2.start()
	p1.start()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def showMsg():
    print("\nFunction: showMsg")
    print("======================")
    print("Servo 0: " + str(Servo0))
    print("Servo 1: " + str(Servo1))
    print("Servo 2: " + str(Servo2))
    print("Servo 3: " + str(Servo3))
    print("Servo 4: " + str(Servo4))
    print("\nloop_degServo1: " + str(loop_degServo1))
    print("loop_degServo2: " + str(loop_degServo2))
    print("loop_degServo3: " + str(loop_degServo3))
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
