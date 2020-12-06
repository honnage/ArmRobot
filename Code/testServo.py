from __future__ import division

import time
import datetime
import RPi.GPIO as GPIO
import sys
import os

import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()


#display = lcddriver.lcd()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.output(11,0)
GPIO.output(13,0)


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


pwm.set_pwm_freq(60)


try:
	servo_min = 500 #deg(= 150) ,45 deg(= 287.5), 90 deg(= 425),180 deg(= 700)
	servo_max = 700
	pwm.set_pwm(4,4,500)
	time.sleep(2)
	for i in range(500,250,-1):
			pwm.set_pwm(4,4,i)
			time.sleep(0.003)
	time.sleep(2)
	for i in range(250,500,1):
			pwm.set_pwm(4,4,i)
			time.sleep(0.003)
	time.sleep(5)



                
                
        
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
    GPIO.cleanup()
