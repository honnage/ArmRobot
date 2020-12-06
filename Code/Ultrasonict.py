import RPi.GPIO as GPIO
import time
import drivers
#import lcdlib

TRIG=14
ECHO=15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#lcd = lcdlib.lcd()

try:
    while True:
        print("distance measurement in progress")
        
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG,False)
        
        #print("waiting for sensor to settle")
        
        time.sleep(0.2)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end-pulse_start
        distance = pulse_duration*17000
        distance = round(distance,2)
        
        dist = str(distance)
        #lcd.lcd_display_string("Distance is",1)
        
        print "distance:",distance,"cm"
        #lcd.lcd_display_string(">>> "+dist+" cm",2)
        #time.sleep(2)
        #lcd.lcd_clear()   
        
        time.sleep(1)
        print("")
    

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleaning up!")
    lcd.lcd_clear()

