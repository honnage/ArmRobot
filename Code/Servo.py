from __future__ import division
import time
import Adafruit_PCA9685
import multiprocessing as mp
import Ultrasonict 
import os
import SetDistance as SetD
import FaceCV

pwm = Adafruit_PCA9685.PCA9685()

print("test")

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


#function default
def default():
    calDeg(0, 0, 10)
    calDeg(1, 0, 15)
    calDeg(2, 0, 0)
    calDeg(3, 0, 85)
    calDeg(4, 0, 90)
	
def default_takkao():
    def default_takkao_channel1(): #servo channel 1
	for i in range(20, 45, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.02)
	    print "default takkao channel 1 ", i

    def default_takkao_channel2(): #servo channel 2
	for i in range(10, 40, 1):
	    calDeg(2, 0, i)
	    time.sleep(0.02)
	    print "default takkao channel 2 ", i
   
    def default_takkao_channel3(): #servo channel 3
	for i in range(60, 90, 1):
	    calDeg(3, 0, i)
	    time.sleep(0.01)
	    print "default takkao channel 3 +", i
    
    calDeg(0, 0, 10)
    calDeg(1, 0, 20)
    calDeg(2, 0, 10)
    calDeg(3, 0, 60)
    calDeg(4, 0, 0)
    default_takkao_channel2()
    default_takkao_channel1()
    default_takkao_channel3()

    time.sleep(0.5)


def scoop_rice():
    def scoop_rice_channel1(): #servo channel 1
	for i in range(45, 60, 1):
	    calDeg(1, 0, i)
	    time.sleep(0.01)
	    print "scoop rice channel 1 +", i
	    
    def scoop_rice_channel3(): #servo channel 3
	for i in range(90, 140, 1):
	    calDeg(3, 0, i)
	    time.sleep(0.01)
	    print "scoop rice channel 3 +", i

    def scoop_rice_channel4(): #servo channel 4
	for i in range(10, 90, 1):
	    calDeg(4, 0, i)
	    time.sleep(0.01)
	    print "scoop rice channel 4 +", i
    
    calDeg(0, 0, 10)
    calDeg(1, 0, 45)
    calDeg(2, 0, 42)
    calDeg(3, 0, 90)
    calDeg(4, 0, 0)
    
    scoop_rice_channel1()
    scoop_rice_channel3()
    scoop_rice_channel4()


def scoop_rice_default():    
    def scoop_rice_default_channel3(): #servo channel 3
	for i in range(105, 90, -1):
	    calDeg(3, 0, i)
	    time.sleep(0.05)
	    print "scoop rice default channel 3 +", i
	    
    calDeg(0, 0, 10)
    calDeg(1, 0, 60)
    calDeg(2, 0, 42)
    calDeg(3, 0, 140)
    calDeg(4, 0, 90)
    scoop_rice_default_channel3()
	    
    
def arm2user():
    for i in range(0, 90, 1):
	calDeg(0, 0, i)

	time.sleep(0.01)
	print "arm to user :",i
    time.sleep(1)
    

def arm2user_fit():
    calDeg(0, 0, 90)
    calDeg(1, 0, 60)
    calDeg(2, 0, 42)
    calDeg(3, 0, 90)
    calDeg(4, 0, 90)
    print 'arm to user fit'
    
def re_standby():
    for i in range(90, 0, -1):
	calDeg(0,0,i)
	time.sleep(0.01)
    time.sleep(1)
    
print('Moving servo on channel 0, press Ctrl-C to quit...')


face = FaceCV.OpenCV()
print(face)
servo_time = 0.001

a = Ultrasonict.Camera()

default()
time.sleep(1)
default_takkao()
scoop_rice()
scoop_rice_default()
time.sleep(0.5)
arm2user()
time.sleep(1)
arm2user_fit()

ser1 = calDeg(1, 0, 60)
ser2 = calDeg(2, 0, 42)
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
time.sleep(4)
re_standby()
default()
    
    




#if(__name__=='__main__'):
    #testservo_1()
    #p1 = mp.Process(target=testservo_1)
    #p2 = mp.Process(target=testservo_2)
    #p1.start()
    #p2.start()
    


    

