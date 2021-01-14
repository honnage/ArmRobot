import RPi.GPIO as GPIO
import time
#import lcdlib
import drivers

# Ultrasonict Canera
TRIG_1 = 23 
ECHO_1 = 24

# Ultrasonict Arm Robot
TRIG_2 = 27 
ECHO_2 = 22 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#lcd = lcdlib.lcd()

try:
    while True:
        print("distance measurement in progress")
        
        GPIO.setup(TRIG_2, GPIO.OUT)
        GPIO.setup(ECHO_2, GPIO.IN)
        GPIO.output(TRIG_2,False)
        
        #print("waiting for sensor to settle")
        
        time.sleep(0.2)
        GPIO.output(TRIG_2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_2, False)
        
        while GPIO.input(ECHO_2) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO_2) == 1:
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
        
        time.sleep(0.5)
        print("")
    

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleaning up!")
    lcd.lcd_clear()

