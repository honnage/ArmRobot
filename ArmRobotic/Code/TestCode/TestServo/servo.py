import RPi.GPIO as GPIO
from time import sleep

servoPIN = 18
s = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(s, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p1 = GPIO.PWM(s, 50)
p.start(0) # Initialization
p1.start(0)
try:
  p1.ChangeDutyCycle(12)
  sleep(0.025)
     
  #while True:
    #p.ChangeDutyCycle(7)
    #sleep(0.025)
  #p1.ChangeDutyCycle(12)

  #p1.ChangeDutyCycle(10)
  #sleep(0.5)
  #p1.ChangeDutyCycle(8)
  #sleep(0.0025)
  
  sleep(1)
  
except KeyboardInterrupt:
  p.stop()
  p1.stop()
  GPIO.cleanup()
