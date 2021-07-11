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
import Ultrasonict
 
print(GPIO.VERSION)
GPIO.setmode(GPIO.BCM)

ledStart = 18 #Yellow
ledWork = 17 #White

GPIO.setup(ledStart, GPIO.OUT)
GPIO.setup(ledWork, GPIO.OUT)

GPIO.output(ledStart, GPIO.HIGH)
print("\nLED Start... ON")

while True:	
	GPIO.output(ledWork, GPIO.HIGH)
	print("\nLED Working... ON")
	time.sleep(1)
	
	GPIO.output(ledWork, GPIO.LOW)
	print("LED Working... OFF")
	time.sleep(3)
