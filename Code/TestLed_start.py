from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import multiprocessing as mp
import Adafruit_PCA9685
import cv2
import numpy as np
import dlib
import math 
import time
import os
#import drivers
print("Start Project ....")
<<<<<<< HEAD
impoxrt Ultrasonict
 
print(GPIO.VERSION)
GPIO.setmode(GPIO.BCM)
ledStart = 18
ledWork = 15
=======
import Ultrasonict
 
print(GPIO.VERSION)
GPIO.setmode(GPIO.BCM)

ledStart = 17
ledWork = 18

>>>>>>> backup

GPIO.setup(ledStart, GPIO.OUT)
GPIO.setup(ledWork, GPIO.OUT)

GPIO.output(ledStart, GPIO.HIGH)
print("\nLED Start... ON")

<<<<<<< HEAD
while True:	
	GPIO.output(ledWork, GPIO.HIGH)
	print("\nLED Working... ON")
	time.sleep(1)
	
	GPIO.output(ledWork, GPIO.LOW)
	print("LED Working... OFF")
=======
try:
	while True:	
		GPIO.output(ledWork, GPIO.HIGH)
		print("\nLED Working... ON")
		time.sleep(1)
		
		GPIO.output(ledWork, GPIO.LOW)
		print("LED Working... OFF")
		time.sleep(3)
		
finally:
	GPIO.cleanup()
	print("\n\nclean up")
>>>>>>> backup
	time.sleep(3)
