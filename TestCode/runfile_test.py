import os
import time
import RPi.GPIO as GPIO
import sys

b = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

OnClick_ButtonRed = 24 #Yello
GPIO.setup(OnClick_ButtonRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

statusButton_Red = 0
try:
	for i in range(3000):
		if GPIO.input(OnClick_ButtonRed) == 0:
			
			b = b+i
			print(b)
			time.sleep(1)
		else:
			c= 1
			#sys.exit("kuy rai a ")
			#exit()
except c == 1:
	exit()
