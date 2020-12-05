import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)
t = 0.0000001

while 1:
    GPIO.output(14, 1)
    time.sleep(0.00001)
    GPIO.output(14, 0)
    trig = 0
    while (GPIO.input(15) == 0) :
            trig = trig + 1
    res = 0
    
    while (GPIO.input(15) == 1):
            res = res + 1
            time.sleep(t)
    distance = (res / 2) * (343.000 / 100) - 2
    print("distance = %5.2f" %(distance))
    time.sleep(0.4)
