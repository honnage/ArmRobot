import RPi.GPIO as GPIO
import time

#-*-codeing: utf8 -*-

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.IN)
GPIO.setup(14, GPIO.OUT)

status = 1

def exit_while(button):
	global status
	status = 0
	
GPIO.add_event_detect(15, GPIO.FALLING, callback=exit_while, bouncetime=300)
while status:
	for i in range(5):
		GPIO.output(14, 1)
		print('loop %d') %(i)
		time.sleep(0.1)
		GPIO.output(14, 0)
		time.sleep(0.1)

GPIO.cleanup
