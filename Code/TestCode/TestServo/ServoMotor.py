from __future__ import division
import time
import math
import Adafruit_PCA9685
import multiprocessing as mp
import Ultrasonict
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
    print("Function: Set Degree Servo Default")
    calDeg(0, 0, 90)
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    
def case_1():
    calDeg(0, 0, 90)
    calDeg(1, 1, 30)
    calDeg(2, 2, 50)
    calDeg(3, 3, 140)
    calDeg(4, 4, 90)

def case_2():
    calDeg(0, 0, 90)
    calDeg(1, 1, 50)
    calDeg(2, 2, 70)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)

def case_3():
    calDeg(0, 0, 90)
    calDeg(1, 1, 70)
    calDeg(2, 2, 90)
    calDeg(3, 3, 120)
    calDeg(4, 4, 90)

def case_4():
    calDeg(0, 0, 90)
    calDeg(1, 1, 90)
    calDeg(2, 2, 110)
    calDeg(3, 3, 120)
    calDeg(4, 4, 90)
    
def case_5():
    calDeg(0, 0, 90)
    calDeg(1, 1, 110)
    calDeg(2, 2, 130)
    calDeg(3, 3, 120)
    calDeg(4, 4, 90)
    
def case_6():
    calDeg(0, 0, 90)
    calDeg(1, 1, 130)
    calDeg(2, 2, 150)
    calDeg(3, 3, 110)
    calDeg(4, 4, 90)
    

while True:
    #x = input("Enter case: ")
    camera_dis = Ultrasonict.Camera()
    x = camera_dis
    print(x)
    
    if x > 0 and x <= 50:
        print("case: 1")
        case_1()
        
    elif x >= 50 and x <= 55:
        print("case: 2") 
        case_2()
        
    elif x >= 55 and x <= 60:
        print("case: 3") 
        case_3()
        
    elif x >= 60 and x <= 65:
        print("case: 4") 
        case_4()
        
    elif x >= 65 and x <= 70:
        print("case: 5") 
        case_5()
    
    elif x >= 70 :
        print("case: 6") 
        case_6()
   
    
    arm_dis = Ultrasonict.Arm()
    time.sleep(0.5)


default()

print(80)
