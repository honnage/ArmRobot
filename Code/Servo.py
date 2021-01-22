from __future__ import division
import time
import Adafruit_PCA9685
import multiprocessing as mp
import Ultrasonict 
import SetDistance as SetD

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
    


print('Moving servo on channel 0, press Ctrl-C to quit...')



#default()
#time.sleep(2)
#takkao()
#SetD.narrow()
#SetD.default()
#SetD.furthest()

Ultrasonict.Camera()
Ultrasonict.Arm()





if(__name__=='__main__'):
    #testservo_1()
    p1 = mp.Process(target=testservo_1)
    p2 = mp.Process(target=testservo_2)
    #p1.start()
    #p2.start()
    


    

