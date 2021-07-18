import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.OUT)

status = 0

while 1:
	if GPIO.input(4) == 1:
		if status == 0:
			GPIO.output(22, 1)
			status = 1
			print("ststus "+str(status))
		
		else:
			GPIO.output(22, 0)
			status = 0
			print("ststus "+str(status))
			
			
	time.sleep(0.1)
GPIO.cleanup
