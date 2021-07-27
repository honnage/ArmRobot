import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.IN)

t = 0.0000001

while 1:
    GPIO.output(22, 1)
    time.sleep(0.00001)
    GPIO.output(22, 0)
    trig = 0
    while (GPIO.input(27) == 0) :
            trig = trig + 1
    res = 0
    
    while (GPIO.input(27) == 1):
            res = res + 1
            time.sleep(t)
    distance = (res / 2) * (343.000 / 100) - 2
    print("distance = %5.2f" %(distance))
    time.sleep(0.4)
