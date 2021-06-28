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
    time.sleep(0.5)
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
    time.sleep(0.5)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_scoop_up():
    calDeg(0, 0, 10)
    calDeg(1, 1, 29)
    calDeg(2, 2, 29)
    calDeg(3, 3, 129)
    calDeg(4, 4, 90)
    print 'Function: arm to fit scoop up'
    time.sleep(0.05)
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
    time.sleep(0.03)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_turn_corner_forward():
    calDeg(0, 0, 90)
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    print 'Function: arm to fit turn corner forward'
    time.sleep(0.05)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def setDegree():
	def distance_detail():
		print("\nDetail Servo working")
		global degServo1, degServo2, degServo3
	
		for i in range(0, 21, 1):
			degServo1 = Servo1 + (loop_degServo1 * i)
			degServo2 = Servo2 + (loop_degServo2 * i)
			degServo3 = Servo3 + (loop_degServo3 * i)
			print("N: " + str(i) + 
			"\t| servo 1: "+ str(degServo1) + 
			" ~ " + str(int(round(degServo1)))+
			"\t| servo 2: "+ str(degServo2) + 
			" ~ " + str(int(round(degServo2)))+
			"\t| servo 3: "+ str(degServo3) + 
			" ~ " + str(int(round(degServo3))))
		print("\n")
		return degServo1, degServo2, degServo3
	
	def setDegree_channel2(): #servo channel 2
		for i in range(0, 21, 1):
			degServo2 = int(round(Servo2 + (loop_degServo2 * i)))
			calDeg(2, 2, degServo2)
			#print("servo 2: N: " + str(i) + "\t| servo 2: "+ str(degServo2))
			time.sleep(time_speack)
			
	def setDegree_channel3(): #servo channel 3
		for i in range(0, 21, 1):
			degServo3 = int(round(Servo3 + (loop_degServo3 * i)))
			calDeg(3, 3, degServo3)
			#print("servo 3: N: " + str(i) + "\t| servo 3: "+ str(degServo3))
			time.sleep(time_speack)
			
	print '\nFunction: set degree'
	Servo0 = 90
	Servo1 = 30
	Servo2 = 30
	Servo3 = 130
	Servo4 = 90
	loop_degServo1 = 0
	loop_degServo2 = 3
	loop_degServo3 = 2.25
	time_speack = 0.045
	
	print("Servo 0: " + str(Servo0))
	print("Servo 1: " + str(Servo1))
	print("Servo 2: " + str(Servo2))
	print("Servo 3: " + str(Servo3))
	print("Servo 4: " + str(Servo4))
	
	print("\nloop_degServo 1: " + str(loop_degServo1))
	print("loop_degServo 2: " + str(loop_degServo2))
	print("loop_degServo 3: " + str(loop_degServo3))
	
	distance_detail()
	if(__name__=='__main__'):
		p2 = mp.Process(target=setDegree_channel2)
		p3 = mp.Process(target=setDegree_channel3)
		p2.start()
		p3.start()
	time.sleep(0.05)
	
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def servo_degree():
	def servo_degree_detail(degree):
	    print("\nDetail Servo working")
	    n = int(degree)
	    #print(n)
	    for i in range(0, n, 1):
		degServo1 = Servo1 + (loop_degServo1 * i)
		degServo2 = Servo2 + (loop_degServo2 * i)
		degServo3 = Servo3 + (loop_degServo3 * i)
		print("N: " + str(i) + 
		"\t| servo 1: "+ str(degServo1) + 
		" ~ " + str(int(round(degServo1)))+
		"\t| servo 2: "+ str(degServo2) + 
		" ~ " + str(int(round(degServo2)))+
		"\t| servo 3: "+ str(degServo3) + 
		" ~ " + str(int(round(degServo3))))
	    print("\n")
	
	def servo_degree_channel1(): #servo channel 1
	    n = int(degree)
	    for i in range(0, n, 1):
		s1 = int(round(Servo1 + (loop_degServo1 * i)))
		calDeg(1, 1, s1)
		print("servo 1: N: " + str(i) + "\t| servo 1: "+ str(s1))
		time.sleep(time_speack)
	
	def servo_degree_channel2(): #servo channel 2
	    n = int(degree)
	    for i in range(0, n, 1):
		s2 = int(round(Servo2 + (loop_degServo2 * i)))
		calDeg(2, 2, s2)
		print("servo 2: N: " + str(i) + "\t| servo 2: "+ str(s2))
		time.sleep(time_speack)
	
	def servo_degree_channel3(): #servo channel 3
	    n = int(degree)
	    for i in range(0, n, 1):
		s3 = int(round(Servo3 + (loop_degServo3 * i)))
		calDeg(3, 3, s3)
		print("servo 3: N: " + str(i) + "\t| servo 3: "+ str(s3))
		time.sleep(time_speack)
	
	print("\nFunction: servo degree")
	print("\ndegree = " + str(average_Camera) + " - 20 ")
	print("degree: " + str(degree))
	
	Servo0 = 90
	Servo1 = 30
	Servo2 = 90
	Servo3 = 175
	Servo4 = 90
	
	loop_degServo1 = 1
	loop_degServo2 = 0.5
	loop_degServo3 = -0.5
	time_speack = 0.05
	
	startServo1 = int(round(degServo1))
	startServo2 = int(round(degServo2))
	startServo3 = int(round(degServo3))
	
	finalServo1 = int(round(degServo1 + (loop_degServo1 * degree)))
	finalServo2 = int(round(degServo2 + (loop_degServo2 * degree)))
	finalServo3 = int(round(degServo3 + (loop_degServo3 * degree)))
	
	print("\nStart Degree servo 1: " + str(startServo1))
	print("Start Degree servo 2: " + str(startServo2))
	print("Start Degree servo 3: " + str(startServo3))
	
	print("\nFinal Degree servo 1: " + str(finalServo1))
	print("Final Degree servo 2: " + str(finalServo2))
	print("Final Degree servo 3: " + str(finalServo3))
	
	print("\nloop_degServo 1: " + str(loop_degServo1))
	print("loop_degServo 2: " + str(loop_degServo2))
	print("loop_degServo 3: " + str(loop_degServo3))
	
	print("\nN = " + str(degree))
	servo_degree_detail(degree)
	
	if(__name__=='__main__'):
		p1 = mp.Process(target=servo_degree_channel1)
		p2 = mp.Process(target=servo_degree_channel2)
		p3 = mp.Process(target=servo_degree_channel3)
		p1.start()
		p2.start()
		p3.start()
	time.sleep(0.05)
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
    time.sleep(0.05)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_turn_back():
    calDeg(0, 0, 90)
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    print 'Function: arm to fit turn_back'
    time.sleep(0.5)
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
    time.sleep(0.05)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print("Run file Servo.py")
'''
time.sleep(1)
default()

time.sleep(1)
default_low()

time.sleep(1)
default_rice()

time.sleep(0.5)
scoop_rice()

time.sleep(0.5)
scoop_up()

time.sleep(0.5)
arm2fit_scoop_up()

time.sleep(0.5)
turn_corner_forward()
'''
time.sleep(0.5)
arm2fit_turn_corner_forward()
'''
average_Camera = Ultrasonict.Camera()
print("Ultrasonic Sensor by camera")
print("Distance: "+ str(round(average_Camera,2)) + " cm\n")

average_Arm = Ultrasonict.Arm()
print("Ultrasonic Sensor by arm")
print("Distance: "+ str(round(average_Arm,2)) + " cm\n")
'''
average_Camera = input("\nEnter average_Arm: ")

while average_Camera < 30 or average_Camera > 71:
    average_Camera = input("\nEnter average_Arm again: ")

print("average_Camera: "+str(average_Camera)+"\n")
degree = int(round(average_Camera - 29))

time.sleep(0.5)
setDegree()

time.sleep(0.5)
servo_degree();

'''
time.sleep(0.5)
print("Process Ultrasonic sensor")
arm_dis = Ultrasonict.Arm()

while average_Arm > 1:
    arm_dis = Ultrasonict.Arm()
    distance = arm_dis
    print("Distance: "+ str(distance) +" cm")
    
    time.sleep(1)
    print("======================")
    
    if distance < 30:
	print("Stop working 6 seconds")
	time.sleep(6)
	print("Stop process Ultrasonic sensor")
	break

time.sleep(0.5)
turn_cornerback(Servo1, Servo2)

time.sleep(1.5)
arm2fit_turn_back()

time.sleep(0.5)
turn_back()

print("======================")

'''
