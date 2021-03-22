from __future__ import division
import time
import Adafruit_PCA9685
import multiprocessing as mp
import Ultrasonict
import os
#import FaceCV

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
    calDeg(1, 0, 20)
    calDeg(2, 0, 0)
    calDeg(3, 0, 85)
    calDeg(4, 0, 90)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def default_rice():
    def default_rice_channel1(): #servo channel 1
	for i in range(20, 45, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.02)

    def default_rice_channel2(): #servo channel 2
	for i in range(10, 50, 1):
	    calDeg(2, 0, i)
	    time.sleep(0.02)
   
    def default_rice_channel3(): #servo channel 3
	for i in range(60, 90, 1):
	    calDeg(3, 0, i)
	    time.sleep(0.02)
	    
    print ("Function: default rice")
    calDeg(0, 0, 10)
    calDeg(1, 0, 20)
    calDeg(2, 0, 10)
    calDeg(3, 0, 60)
    calDeg(4, 0, 0)
    
    default_rice_channel2()
    default_rice_channel1()
    default_rice_channel3()
    time.sleep(0.5)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def scoop_rice():
    def scoop_rice_channel1(): #servo channel 1
	for i in range(45, 90, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.02)
	    
    def scoop_rice_channel3(): #servo channel 3
	for i in range(90, 140, 1):
	    calDeg(3, 0, i)
	    time.sleep(0.02)
    
    def scoop_rice_channel4(): #servo channel 4
	for i in range(0, 90, 1):
	    calDeg(4, 0, i)
	    time.sleep(0.01)

    print ("Function: scoop rice")
    calDeg(0, 0, 10)
    calDeg(1, 0, 45)
    calDeg(2, 0, 50)
    calDeg(3, 0, 90)
    calDeg(4, 0, 0)
    
    if(__name__=='__main__'):
	p3 = mp.Process(target=scoop_rice_channel3)
	p1 = mp.Process(target=scoop_rice_channel1)
	p3.start()
	p1.start()
    
    time.sleep(0.5)
    scoop_rice_channel4()
    time.sleep(0.5)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def scoop_up():    
    def scoop_up_channel3(): #servo channel 3
	for i in range(141, 100, -1):
	    calDeg(3, 0, i)
	    time.sleep(0.05)
    
    def scoop_up_channel2(): #servo channel 2
	for i in range(42, 90, 1):
	    calDeg(2, 0, i)
	    time.sleep(0.03)
    
    print ("Function: scoop up")
    calDeg(0, 0, 10)
    calDeg(1, 0, 90)
    calDeg(2, 0, 50)
    calDeg(3, 0, 140)
    calDeg(4, 0, 90)
    
    scoop_up_channel3()
    time.sleep(0.05)
    scoop_up_channel2()
    time.sleep(0.05)
    '''
    if(__name__=='__main__'):
	p3 = mp.Process(target=scoop_up_channel3)
	p2 = mp.Process(target=scoop_up_channel2)
	p3.start()
	p2.start()
    '''
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_corner_forward():
    def turn_corner_forward_channel0(): #servo channel 0
	for i in range(10, 90, 1):
	    calDeg(0, 0, i)
	    time.sleep(0.03)
	    
    print ("Function: turn corner forward")
    calDeg(0, 0, 10)
    calDeg(1, 0, 90)
    calDeg(2, 0, 90)
    calDeg(3, 0, 100)
    calDeg(4, 0, 90)
    turn_corner_forward_channel0()
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def turn_back():
    def turn_back_channel0(): #servo channel 0
	for i in range(90, 10, -1):
	    calDeg(0, 0, i)
	    time.sleep(0.03)

    print ("Function: turn back")
    calDeg(0, 0, 10)
    calDeg(1, 0, 90)
    calDeg(2, 0, 90)
    calDeg(3, 0, 100)
    calDeg(4, 0, 90)
    turn_back_channel0()
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit():
    calDeg(0, 0, 90)
    calDeg(1, 0, 90)
    calDeg(2, 0, 90)
    calDeg(3, 0, 100)
    calDeg(4, 0, 90)
    print 'Function: arm to fit'
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

default_rice()
scoop_rice()
'''
time.sleep(1)
default()

time.sleep(2)
default_rice()

time.sleep(0.1)
scoop_rice()

time.sleep(0.1)
scoop_up()

time.sleep(0.1)
turn_corner_forward()

time.sleep(0.1)
arm2fit()

time.sleep(1)

servo1 = calDeg(1, 0, 90)
servo2 = calDeg(2, 0, 90)

time.sleep(1)
arm_dis = Ultrasonict.check_extra()
while arm_dis >= 20:
    arm_dis = Ultrasonict.check_extra()
    print(arm_dis)
    if servo1 <= 180:
	servo1 += 1
	calDeg(1, 0, servo1)
	time.sleep(0.1)
	print("servo 1 deg: "+str(servo1))
	
    if servo2 <= 180:
	servo2 += 1
	calDeg(2, 0, servo2)
	time.sleep(0.1)
	print("serv0 2 deg: "+str(servo2))
    
    print(" ")

time.sleep(2)

arm_dis = Ultrasonict.check_extra()
while arm_dis < 20:
    arm_dis = Ultrasonict.check_extra()

print('ok ')
#turn_back()

#test()
'''
'''
def test_cannel1(): #servo channel 1
	for i in range(0, 180, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.02)

test_cannel1()
'''
'''
calDeg(1, 0, 0)
calDeg(2, 0, 0)
'''
