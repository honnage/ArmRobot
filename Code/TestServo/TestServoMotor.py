import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings (False)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)
p.start(0)

try:

	p.ChangeDutyCycle(1.5)
	time.sleep(1)
		
	

except KeyboardInterrupt:
	GPIO.cleanup()

