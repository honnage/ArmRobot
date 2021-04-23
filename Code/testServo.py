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
def default():
    calDeg(0, 0, 10)
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 85)
    calDeg(4, 4, 90)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def default_low():
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
    time.sleep(0.5)
    
    #default_low_channel2()

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
    time.sleep(0.5)

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
    time.sleep(0.5)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def scoop_up():    
    def scoop_up_channel3(): #servo channel 3
	for i in range(141, 100, -1):
	    calDeg(3, 3, i)
	    time.sleep(0.05)
    
    def scoop_up_channel2(): #servo channel 2
	for i in range(50, 90, 1):
	    calDeg(2, 2, i)
	    time.sleep(0.03)
	    #print("deg servo 2 "+str(i))
    
    print ("Function: scoop up")
    calDeg(0, 0, 10)
    calDeg(1, 1, 90)
    calDeg(2, 2, 50)
    calDeg(3, 3, 140)
    calDeg(4, 4, 90)
    
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
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 100)
    calDeg(4, 4, 90)
    
    turn_corner_forward_channel0()
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit():
    calDeg(0, 0, 90)
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 100)
    calDeg(4, 4, 90)
    print 'Function: arm to fit'
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_cornerback(s1, s2):
    print 'Function: turn cornerback'
    print ("Value servo 1 = " + str(s1))
    print ("Value servo 2 = " + str(s2))
    
    def turn_cornerback_channel1(): #servo channel 1
	for i in range(s1, 90, -1):
	    calDeg(1, 0, i)
	    print("servo 1 deg: "+str(i))
	    time.sleep(0.03)
	
	
    def turn_cornerback_channel2(): #servo channel 2
	for i in range(s2, 90, -1):
	    calDeg(2, 0, i)
	    print("servo 2 deg: "+str(i))
	    time.sleep(0.03)
	
	    
    calDeg(3, 3, 100)
    calDeg(4, 4, 90)
    #turn_cornerback_channel1()
    #turn_cornerback_channel2()
    
    if(__name__=='__main__'):
	p2 = mp.Process(target=turn_cornerback_channel2)
	p1 = mp.Process(target=turn_cornerback_channel1)
	
	p2.start()
	p1.start()
    
    time.sleep(0.05)
    
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_back():
    def turn_back_channel0(): #servo channel 0
	for i in range(90, 10, -1):
	    calDeg(0, 0, i)
	    time.sleep(0.01)

    print ("Function: turn back")
    calDeg(0, 0, 10)
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 100)
    calDeg(4, 4, 90)
    turn_back_channel0()
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

default()
time.sleep(1)

default_low()
time.sleep(0.5)

time.sleep(0.1)
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

servo1 = calDeg(1, 1, 90)
servo2 = calDeg(2, 2, 90)

time.sleep(0.5)
print("Ultrasonic sensor")
arm_dis = Ultrasonict.check_extra()
while arm_dis >= 20:
    arm_dis = Ultrasonict.check_extra()
    print(arm_dis)
    if servo1 < 150:
	servo1 += 1
	calDeg(1, 1, servo1)
	print("servo 1 deg: " + str(servo1))
	
    elif servo1 == 180:
	calDeg(1, 1, 180)
	
    if servo2 < 150:
	servo2 += 1
	calDeg(2, 2, servo2)
	print("servo 2 deg: " + str(servo2))
	
    elif servo2 == 180:
	calDeg(2, 2, 180)
	
    print("======================")

time.sleep(0.5)
arm_dis = Ultrasonict.check_extra()
while arm_dis < 20:
    arm_dis = Ultrasonict.check_extra()

print('ok ')
time.sleep(5)
turn_cornerback(servo1, servo2)

time.sleep(0.5)
turn_back()

#test()


