import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.IN)
GPIO.setup(14, GPIO.OUT)
status = 0

while 1:
	if GPIO.input(15) == 1:
		GPIO.output(14, 1)
		time.sleep(0.2)
		GPIO.output(14, 0)

GPIO.cleanup
