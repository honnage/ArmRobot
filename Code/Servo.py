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

a = Ultrasonict.Camera()

DEG.default()
time.sleep(1)
DEG.default_takkao()
DEG.scoop_rice()
DEG.scoop_rice_default()
time.sleep(0.003)
DEG.make_angle()
time.sleep(0.001)
DEG.arm2user()
#time.sleep(0.001)
DEG.arm2user_fit()

ser1 = calDeg(1, 0, 90)
ser2 = calDeg(2, 0, 80)

b = Ultrasonict.Camera()
print b
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
    
DEG.arm2user_fit()
time.sleep(0.005)
DEG.re_standby()
DEG.re_default()
time.sleep(0.5)
DEG.default()
time.sleep(1)


    


    

