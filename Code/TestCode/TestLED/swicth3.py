import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.IN)
GPIO.setup(14, GPIO.OUT)

status = 0

while 1:
	if GPIO.input(15) == 1:
		if status == 0:
			GPIO.output(14, 1)
			status = 1
			print("ststus "+str(status))
		
		else:
			GPIO.output(14, 0)
			status = 0
			print("ststus "+str(status))
			
			
	time.sleep(0.1)
GPIO.cleanup
