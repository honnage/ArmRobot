from __future__ import division
import time
import math
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import multiprocessing as mp
import Ultrasonict
import os
import SetDegree as sd
import DisplayLCD  as dp
import drivers


GPIO.cleanup()
display = drivers.Lcd()
pwm = Adafruit_PCA9685.PCA9685()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# --- Set GPIO ---
LED_Green = 27 #Green
LED_Yello = 22 #Yello

OnClick_ButtonGreen = 23 #Orange
OnClick_ButtonRed = 24 #Yello
Onclick_ButtonEmergent = 4 #Broen 

GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(LED_Yello, GPIO.OUT)

GPIO.setup(OnClick_ButtonGreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(OnClick_ButtonRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Onclick_ButtonEmergent, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

statusWorking_LEDGreen = 0
statusWorking_LEDYello = 0

statusButton_Green = 0
statusButton_Red = 0
statusButton_Emergent = 0

GPIO.output(LED_Green, GPIO.LOW)
GPIO.output(LED_Yello, GPIO.LOW)

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
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def calDeg(a,b,c):
    statusWorking_LEDGreen = 1
    statusWorking_LEDYello = 0
    statusButton_Green = 0
    statusButton_Red = 0
    statusButton_Emergent = 0
    
    if GPIO.input(OnClick_ButtonRed) == 1:
	time.sleep(0.1)
	#default()
	isWorking = False
	dp.onClickButtonRed()
	exit()
	return isWorking
    
    #onClick Button Emergent: ON 
    if GPIO.input(Onclick_ButtonEmergent) == 0:
	statusWorking_LEDGreen = 0
	statusWorking_LEDYello = 1
	statusButton_Green = 0
	statusButton_Red = 0
	statusButton_Emergent = 1
	
	GPIO.output(LED_Green, GPIO.LOW)
	GPIO.output(LED_Yello, GPIO.HIGH)
	print("\nYello LED Working... ON")
	time.sleep(0.2)
	
	GPIO.output(LED_Yello, GPIO.LOW)
	print("\nYello LED Working... OFF")
	time.sleep(0.2)
	
	dp.onClickButtonEmergency_on()
	time.sleep(0.3)
	display.lcd_clear()
	
    if GPIO.input(OnClick_ButtonGreen) == 1 and  statusButton_Emergent == 1:
	pass
	    
		    
    #onClick Button Emergent: OFF	
    if GPIO.input(Onclick_ButtonEmergent) == 1 and  statusButton_Emergent == 1:
	display.lcd_clear()
	statusWorking_LEDGreen = 0
	statusWorking_LEDYello = 0
	statusButton_Green = 0
	statusButton_Red = 0
	statusButton_Emergent = 0
	GPIO.output(LED_Green, GPIO.LOW)
	GPIO.output(LED_Yello, GPIO.LOW)
	
	print("\nOnClick Button Emergent: OFF\n")
	print("="*30)
	    
		
    else:
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
    time.sleep(1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def default_rice():
    calDeg(0, 0, 10)
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 85)
    calDeg(4, 4, 90)
    
    def default_rice_channel1(): #servo channel 1
	for i in range(90, 45, -1):
	    calDeg(1, 1, i)
	    time.sleep(0.02)
	    
    def default_rice_channel2(): #servo channel 2
	for i in range(90, 50, -1):
	    calDeg(2, 2, i)
	    time.sleep(0.02)
    
    def default_rice_channel3(): #servo channel 3
	for i in range(60, 90, 1):
	    calDeg(3, 3, i)
	    time.sleep(0.03)
    
    if(__name__=='__main__'):
	p3 = mp.Process(target=default_rice_channel3)
	p2 = mp.Process(target=default_rice_channel2)
	p1 = mp.Process(target=default_rice_channel1)
	
	p2.start()
	p1.start()
	p3.start()

    time.sleep(1)
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
	for i in range(90, 39, -1):
	    calDeg(1, 1, i)
	    print("servo 1 deg: "+str(i))
	    time.sleep(0.05)

    def scoop_up_channel3(): #servo channel 3
	for i in range(141, 129, -1):
	    calDeg(3, 3, i)
	    print("servo 3 deg: "+str(i))
	    time.sleep(0.05)

    if(__name__=='__main__'):
	p3 = mp.Process(target=scoop_up_channel3)
	p1 = mp.Process(target=scoop_up_channel1)
	p3.start()
	p1.start()
    time.sleep(1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_scoop_up():
    calDeg(0, 0, 10)
    calDeg(1, 1, 40)
    calDeg(2, 2, 50)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    print 'Function: arm to fit scoop up'
    time.sleep(0.5)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_corner_forward():
    def turn_corner_forward_channel0(): #servo channel 0
	for i in range(10, 90, 1):
	    calDeg(0, 0, i)
	    time.sleep(0.02)
	    
    print ("Function: turn corner forward")
    time.sleep(1)
    calDeg(0, 0, 10)
    calDeg(1, 1, 40)
    calDeg(2, 2, 50)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    
    turn_corner_forward_channel0()
    time.sleep(1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def arm2fit_turn_corner_forward():
    calDeg(0, 0, 90)
    calDeg(1, 1, 40)
    calDeg(2, 2, 50)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    print 'Function: arm to fit turn corner forward'
    time.sleep(0.5)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def distance_case(loop_degServo1, loop_degServo2, loop_degServo3, time_case):
    print '\nFunction: distance case'
    print("time_case: "+str(time_case))
    calDeg(0, 0, 90)
    calDeg(1, 1, 40)
    calDeg(2, 2, 50)
    calDeg(3, 3, 130)
    calDeg(4, 4, 90)
    
    start_servo1 = 40
    start_servo2 = 50
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
    time_speack = time_speack + time_case
    print("time_case: "+str(time_speack))
    
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
    time.sleep(1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def turn_back():
    def turn_back_channel0(): #servo channel 0
	for i in range(90, 10, -1):
	    calDeg(0, 0, i)
	    time.sleep(0.01)
    
    print ("Function: turn back")
    print("Servo 0: " + str(Servo0))
    print("Servo 1: " + str(Servo1))
    print("Servo 2: " + str(Servo2))
    print("Servo 3: " + str(Servo3))
    print("Servo 4: " + str(Servo4))
    
    calDeg(0, 0, 90)
    turn_back_channel0()
    calDeg(1, 1, 90)
    calDeg(2, 2, 90)
    calDeg(3, 3, 90)
    calDeg(4, 4, 90)
   
    time.sleep(1)
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

time.sleep(0.5)
print("Run file Servo.py")
dp.servoWorking()
sd.default()

time.sleep(1)
default()

time.sleep(1)
default_rice()

time.sleep(1)
scoop_rice()

time.sleep(1)
scoop_up()

time.sleep(1)
arm2fit_scoop_up()

time.sleep(1)
turn_corner_forward()

time.sleep(1)
arm2fit_turn_corner_forward()

average_Camera = Ultrasonict.Camera()
print("Ultrasonic Sensor by camera")
print("Distance: "+ str(round(average_Camera,2)) + " cm\n")

average_Arm = Ultrasonict.Arm()
print("Ultrasonic Sensor by arm")
'''
average_Camera = input("\nEnter average_Camera: ")
print("Distance: "+ str(round(average_Camera,2)) + " cm\n")
'''
time.sleep(0.5)


if average_Camera > 0 and average_Camera < 50:
    print("case: 1")
    print("distance >= 0 and distance <= 50")

    Servo0 = 90
    Servo1 = 60
    Servo2 = 80
    Servo3 = 130
    Servo4 = 90
    
    loop_degServo1 = 1
    loop_degServo2 = 1.5
    loop_degServo3 = 0
    time_case = 0
    
    showMsg()
    distance_case(loop_degServo1, loop_degServo2, loop_degServo3, time_case) 
	
elif average_Camera >= 50 and average_Camera < 55:
    print("case: 2") 
    print("distance >= 50 and distance <= 55")

    Servo0 = 90
    Servo1 = 70
    Servo2 = 90
    Servo3 = 130 
    Servo4 = 90
    
    loop_degServo1 = 1.5
    loop_degServo2 = 2
    loop_degServo3 = 0
    time_case = 0.005
    
    showMsg()
    distance_case(loop_degServo1, loop_degServo2, loop_degServo3, time_case) 

    
elif average_Camera >= 55 and average_Camera < 60:
    print("case: 3") 
    print("distance >= 55 and distance <= 60")
    
    Servo0 = 90
    Servo1 = 80
    Servo2 = 100
    Servo3 = 120 
    Servo4 = 90
    
    loop_degServo1 = 2
    loop_degServo2 = 2.5
    loop_degServo3 = -0.5
    time_case = 0.01
  
    showMsg()
    distance_case(loop_degServo1, loop_degServo2, loop_degServo3, time_case) 

elif average_Camera >= 60 and average_Camera < 65:
    print("case: 4") 
    print("distance >= 60 and distance <= 65")

    Servo0 = 90
    Servo1 = 90
    Servo2 = 110
    Servo3 = 120 
    Servo4 = 90
    
    loop_degServo1 = 2.5
    loop_degServo2 = 3
    loop_degServo3 = -0.5
    time_case = 0.015
    
    showMsg()
    distance_case(loop_degServo1, loop_degServo2, loop_degServo3, time_case) 
    
elif average_Camera >= 65 and average_Camera < 70:
    print("case: 5") 
    print("distance >= 65 and distance <= 70")
    
    Servo0 = 90
    Servo1 = 100
    Servo2 = 120
    Servo3 = 120 
    Servo4 = 90
    
    loop_degServo1 = 3
    loop_degServo2 = 3.5
    loop_degServo3 = -0.5
    time_case = 0.02
  
    showMsg()
    distance_case(loop_degServo1, loop_degServo2, loop_degServo3, time_case)  


elif average_Camera >= 70:
    print("case: 6") 
    print("distance >= 65")

    Servo0 = 90
    Servo1 = 110
    Servo2 = 130
    Servo3 = 110 
    Servo4 = 90
    
    loop_degServo1 = 3.5
    loop_degServo2 = 4
    loop_degServo3 = -1
    time_case = 0.025
  
    showMsg()
    distance_case(loop_degServo1, loop_degServo2, loop_degServo3, time_case) 

time.sleep(0.5)
print("Process Ultrasonic sensor")
arm_dis = Ultrasonict.Arm()

while average_Arm > 0:
    arm_dis = Ultrasonict.Arm()
    distance = arm_dis
    print("Distance: "+ str(distance) +" cm")
    
    time.sleep(0.1)
    print("======================")
    
    if distance < 30:
	print("Stop working 6 seconds")
	time.sleep(6)
	print("Stop process Ultrasonic sensor")
	break


time.sleep(1)
turn_back()

time.sleep(1)
print("======================")
#GPIO.cleanup()


