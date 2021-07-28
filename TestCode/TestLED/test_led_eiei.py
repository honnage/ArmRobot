import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)
i = 0;
while True:
	GPIO.output(13,True)
	time.sleep(1)
	GPIO.output(13,False)
	i = i+1;
	print(i)
	time.sleep(1)
	

GPIO.output(13,False)
