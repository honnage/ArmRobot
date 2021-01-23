from __future__ import division
import time
import Adafruit_PCA9685
import multiprocessing as mp
import Ultrasonict 
import os
import SetDegree as DEG
import FaceCV

pwm = Adafruit_PCA9685.PCA9685()

print("Run File Servo.py")
    
pwm.set_pwm_freq(60)


def calDeg(a,b,c):
	re_deg = c
	degree = 2.77*c
	degree = degree+100
	degree = int(degree)
	pwm.set_pwm(a,b,degree)
	return re_deg


print('Moving servo on channel 0, press Ctrl-C to quit...')

face = FaceCV.OpenCV()
print(face)

DEG.main()
    

