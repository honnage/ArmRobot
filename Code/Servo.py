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
def distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3):
    print '\nFunction: distance case'
    calDeg(1, 1, 30)
    calDeg(2, 2, 30)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    
    #Debug Value
    #print("\nloop_degServo1: " + str(loop_degServo1))
    #print("loop_degServo2: " + str(loop_degServo2))
    #print("loop_degServo3: " + str(loop_degServo3))
    
    start_servo1 = 30
    start_servo2 = 30
    start_servo3 = 130
    
    def distance_detail():
	print("\nDetail Servo working")
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
    
    def distance_case_channel1():
	for i in range(0, 21, 1):
	    degServo1 = int(math.ceil(start_servo1 + (loop_degServo1 * i)))
	    calDeg(1, 1, degServo1)
	    print("servo 1: N: " + str(i) + "\t| servo 1: "+ str(degServo1))
	    time.sleep(0.025)
    
    def distance_case_channel2():
	for i in range(0, 21, 1):
	    degServo2 = int(math.ceil(start_servo2 + (loop_degServo2 * i)))
	    calDeg(2, 2, degServo2)
	    print("servo 2: N: " + str(i) + "\t| servo 2: "+ str(degServo2))
	    time.sleep(0.025)
    
    def distance_case_channel3():
	for i in range(0, 21, 1):
	    degServo3 = int(math.ceil(start_servo3 + (loop_degServo3 * i)))
	    calDeg(3, 3, degServo3)
	    print("servo 3: N: " + str(i) + "\t| servo 3: "+ str(degServo3))
	    time.sleep(0.025)
    
    distance_detail()    
    
    if(__name__=='__main__'):
	p1 = mp.Process(target=distance_case_channel1)
	p2 = mp.Process(target=distance_case_channel2)
	p3 = mp.Process(target=distance_case_channel3)
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
def showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3):
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
print("Run file Servo.py")

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

time.sleep(0.5)
arm2fit_turn_corner_forward()

average_Camera = Ultrasonict.Camera()
print("Ultrasonic Sensor by camera")
print("Distance: "+ str(round(average_Camera,2)) + " cm\n")

average_Arm = Ultrasonict.Arm()
print("Ultrasonic Sensor by arm")
print("Distance: "+ str(round(average_Arm,2)) + " cm\n")

#average_Camera = input("\nEnter average_Arm: ")
time.sleep(0.5)
print("average_Camera: "+str(average_Camera)+"\n")

if average_Camera > 0 and average_Camera <= 30:
    print("case: 1")
    print("distance >= 0 and distance <= 30")

    Servo0 = 90
    Servo1 = 30
    Servo2 = 90
    Servo3 = 175 
    Servo4 = 90
    
    loop_degServo1 = 0
    loop_degServo2 = 3
    loop_degServo3 = 2.25
    
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 
	
elif average_Camera >= 30 and average_Camera <= 35:
    print("case: 2") 
    print("distance >= 30 and distance <= 35")

    Servo0 = 90
    Servo1 = 40
    Servo2 = 95
    Servo3 = 170 
    Servo4 = 90
    
    loop_degServo1 = 0.5
    loop_degServo2 = 3.25
    loop_degServo3 = 2
  
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 

    
elif average_Camera >= 35 and average_Camera <= 40:
    print("case: 3") 
    print("distance >= 35 and distance <= 40")
    
    Servo0 = 90
    Servo1 = 50
    Servo2 = 100
    Servo3 = 165 
    Servo4 = 90
    
    loop_degServo1 = 1
    loop_degServo2 = 3.5
    loop_degServo3 = 1.75
  
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 

elif average_Camera >= 40 and average_Camera <= 45:
    print("case: 4") 
    print("distance >= 50 and distance <= 60")

    Servo0 = 90
    Servo1 = 60
    Servo2 = 105
    Servo3 = 160 
    Servo4 = 90
    
    loop_degServo1 = 1.5
    loop_degServo2 = 3.75
    loop_degServo3 = 1.5
    
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 
    
elif average_Camera >= 45 and average_Camera <= 50:
    print("case: 5") 
    print("distance >= 45 and distance <= 50")
    
    Servo0 = 90
    Servo1 = 70
    Servo2 = 110
    Servo3 = 155 
    Servo4 = 90
    
    loop_degServo1 = 2
    loop_degServo2 = 4
    loop_degServo3 = 1.25
  
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 

elif average_Camera >= 50 and average_Camera <= 55:
    print("case: 6") 
    print("distance >= 50 and distance <= 55")
    
    Servo0 = 90
    Servo1 = 80
    Servo2 = 115
    Servo3 = 150 
    Servo4 = 90
    
    loop_degServo1 = 2.5
    loop_degServo2 = 4.25
    loop_degServo3 = 1
  
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 

elif average_Camera >= 55 and average_Camera <= 60:
    print("case: 7") 
    print("distance >= 55 and distance <= 60")
    
    Servo0 = 90
    Servo1 = 90
    Servo2 = 120
    Servo3 = 145 
    Servo4 = 90
    
    loop_degServo1 = 3
    loop_degServo2 = 4.5
    loop_degServo3 = 0.75
  
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 

elif average_Camera >= 60 and average_Camera <= 65:
    print("case: 8") 
    print("distance >= 60 and distance <= 65")
    
    Servo0 = 90
    Servo1 = 100
    Servo2 = 125
    Servo3 = 140 
    Servo4 = 90
    
    loop_degServo1 = 3.5
    loop_degServo2 = 4.75
    loop_degServo3 = 0.5
  
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 
    
elif average_Camera >= 65:
    print("case: 9") 
    print("distance >= 65")

    Servo0 = 90
    Servo1 = 110
    Servo2 = 130
    Servo3 = 135 
    Servo4 = 90
    
    loop_degServo1 = 4
    loop_degServo2 = 5
    loop_degServo3 = 0.25
  
    showMsg(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3)
    distance_case(Servo0, Servo1, Servo2, Servo3, Servo4, loop_degServo1, loop_degServo2, loop_degServo3) 

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

