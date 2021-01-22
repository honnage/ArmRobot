from __future__ import division
import time
import Adafruit_PCA9685
import multiprocessing as mp
import Ultrasonict as Ulta

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
	degree = 2.77*c
	degree = degree+100
	degree = int(degree)
	pwm.set_pwm(a,b,degree)

#function default
def default():
    calDeg(0, 0, 10)
    calDeg(1, 0, 45)
    calDeg(2, 0, 40)
    calDeg(3, 0, 135)
    calDeg(4, 0, 90)
    
#function default
def takkao():
    calDeg(0, 0, 10)
    calDeg(1, 0, 65)
    calDeg(2, 0, 20)
    calDeg(3, 0, 135)
    calDeg(4, 0, 90)

#Make the furthest corner
def furthest():
    calDeg(0, 0, 90)
    calDeg(1, 0, 170)
    calDeg(2, 0, 165)
    calDeg(3, 0, 90)
    calDeg(4, 0, 90)

#Make the narrow angle
def narrow():
    calDeg(0, 0, 90)
    calDeg(1, 0, 20)
    calDeg(2, 0, 0)
    calDeg(3, 0, 90)
    calDeg(4, 0, 90)

#Make the shortest angle
def shortest():
    calDeg(0, 0, 90)
    calDeg(1, 0, 20)
    calDeg(2, 0, 80)
    calDeg(3, 0, 180)
    calDeg(4, 0, 90)
        
def testservo_1():
    pwm.set_pwm(1, 0, 170)
    time.sleep(2)
    for i in range(170,250,1):
	    pwm.set_pwm(1, 0, i)
	    time.sleep(0.005)
	    
    time.sleep(2)
    for i in range(250,150,-1):
	    pwm.set_pwm(1,0,i)
	    time.sleep(0.005)
    time.sleep(5)

def testservo_2():
    pwm.set_pwm(2, 0, 200)
    time.sleep(2)
    for i in range(200,300,1):
	    pwm.set_pwm(2,0,i)
	    time.sleep(0.005)
    time.sleep(2)
    for i in range(300,200,-1):
	    pwm.set_pwm(2,0,i)
	    time.sleep(0.005)
    time.sleep(5)
    
def testservo_3():
    pwm.set_pwm(3, 0, 500)
    time.sleep(2)
    for i in range(500,400,-1):
	    pwm.set_pwm(3,0,i)
	    time.sleep(0.005)
    time.sleep(2)
    for i in range(400,500,1):
	    pwm.set_pwm(3,0,i)
	    time.sleep(0.005)
    time.sleep(5)

print('Moving servo on channel 0, press Ctrl-C to quit...')

#default()
#time.sleep(2)
#takkao()
#furthest()
#narrow()
#shortest()
distanceA = 34.71
distanceA = 27.7
while True:
    shortest()
    Ulta.Arm()
    furthest()
    Ulta.Camera()
    narrow()
    time.sleep(1)


if(__name__=='__main__'):
    #testservo_1()
    p1 = mp.Process(target=testservo_1)
    p2 = mp.Process(target=testservo_2)
    p3 = mp.Process(target=testservo_3)
    #p1.start()
    #p2.start()
    #p3.start()


    

